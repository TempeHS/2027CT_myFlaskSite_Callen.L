import pytest
from app import app
from search_service import sanitize_search_query, SEARCH_PAGES


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config["TESTING"] = True
    with app.test_client() as test_client:
        yield test_client


def get_testable_routes():
    """Return all GET routes without URL params, excluding static."""
    routes = []
    for rule in app.url_map.iter_rules():
        if "GET" not in rule.methods:
            continue
        if rule.endpoint == "static":
            continue
        if rule.arguments:
            continue
        routes.append(rule.rule)
    return sorted(set(routes))


@pytest.mark.parametrize("route", get_testable_routes())
def test_all_get_routes_return_success(client, route):
    response = client.get(route)
    if response.status_code in (301, 302, 307, 308):
        response = client.get(route, follow_redirects=True)
    assert response.status_code == 200


@pytest.mark.parametrize(
    "query",
    [
        "home",
        "contact",
        "about",
        "privacy",
        "support",
        "brawlers",
        "rare",
        "bounty",
    ],
)
def test_search_redirect_immediate(client, query):
    response = client.get(f"/search?q={query}", follow_redirects=True)
    assert response.status_code == 200


def test_404_page(client):
    response = client.get("/this-page-does-not-exist")
    assert response.status_code == 404


def test_sanitizing_blank_spaces():
    assert sanitize_search_query("   hello world   ") == "hello world"


def test_sanitizing_special_characters():
    assert sanitize_search_query("<script>alert(1)</script>") == "scriptalert1script"


def test_sanitize_limits_length():
    query = "a" * 200
    assert len(sanitize_search_query(query)) == 80


def all_search_terms():
    seen = set()

    for page in SEARCH_PAGES:
        endpoint = page.get("endpoint")
        title = page.get("title", "")
        keywords = page.get("keywords", [])

        if endpoint and endpoint not in seen:
            seen.add(endpoint)
            yield endpoint

        if title and title not in seen:
            seen.add(title)
            yield title

        for keyword in keywords:
            if keyword and keyword not in seen:
                seen.add(keyword)
                yield keyword


@pytest.mark.parametrize("term", list(all_search_terms()))
def test_every_search_term(client, term):
    response = client.get(f"/search?q={term}", follow_redirects=True)
    assert response.status_code == 200


def test_search_without_query_returns_200(client):
    response = client.get("/search")
    assert response.status_code == 200


def test_search_whitespace_query_does_not_redirect(client):
    response = client.get("/search?q=   ")
    assert response.status_code == 200


def test_search_exact_match_is_case_insensitive_redirect(client):
    response = client.get("/search?q=HoMe")
    assert response.status_code == 302


def test_sanitize_preserves_allowed_chars():
    assert sanitize_search_query("O'Neil_test-name") == "O'Neil_test-name"


def test_sanitize_collapses_mixed_whitespace():
    assert sanitize_search_query("a\t b\n  c") == "a b c"


def test_search_pages_endpoints_exist_in_app():
    for page in SEARCH_PAGES:
        assert page["endpoint"] in app.view_functions


def test_search_pages_have_unique_endpoints():
    endpoints = [page["endpoint"] for page in SEARCH_PAGES]
    assert len(endpoints) == len(set(endpoints))
