import pytest
from app import app
from search_service import sanitize_search_query, SEARCH_PAGES


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config["TESTING"] = True
    with app.test_client() as test_client:
        yield test_client


def endpoint_to_path(endpoint: str) -> str:
    """Resolve an endpoint to a concrete URL path without pushing request context."""
    for rule in app.url_map.iter_rules(endpoint):
        if not rule.arguments:
            return rule.rule
    raise AssertionError(f"No concrete route found for endpoint: {endpoint}")


def get_testable_routes():
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


def test_search_exact_match_redirect_location(client):
    response = client.get("/search?q=home", follow_redirects=False)
    assert response.status_code in (301, 302, 307, 308)
    assert response.headers["Location"].endswith("/")


def test_search_unknown_query_returns_page(client):
    response = client.get("/search?q=zzzz-no-match-12345")
    assert response.status_code == 200


def test_search_result_page_renders_query(client):
    response = client.get("/search?q=brawl")
    assert response.status_code == 200
    assert b"brawl" in response.data.lower()


def test_search_pages_have_required_fields():
    for page in SEARCH_PAGES:
        assert isinstance(page.get("endpoint"), str) and page["endpoint"].strip()
        assert isinstance(page.get("title"), str) and page["title"].strip()
        assert isinstance(page.get("description"), str) and page["description"].strip()
        assert isinstance(page.get("keywords"), list)


def test_search_page_endpoints_can_build_urls():
    for page in SEARCH_PAGES:
        path = endpoint_to_path(page["endpoint"])
        assert isinstance(path, str) and path.startswith("/")


# Search safety


def test_get_routes_do_not_accept_post():
    """Safety Test: GET pages should not silently accept POST."""
    for rule in app.url_map.iter_rules():
        if rule.endpoint == "static" or rule.arguments:
            continue
        if "GET" in rule.methods:
            assert "POST" not in rule.methods


def test_every_search_page_endpoint_returns_success(client):
    """Each SEARCH_PAGES endpoint should render successfully."""
    for page in SEARCH_PAGES:
        url = endpoint_to_path(page["endpoint"])
        response = client.get(url)
        if response.status_code in (301, 302, 307, 308):
            response = client.get(url, follow_redirects=True)
        assert response.status_code == 200


def test_search_handles_very_long_query(client):
    response = client.get("/search?q=" + ("x" * 5000))
    assert response.status_code == 200


def test_home_route_is_stable(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"<html" in response.data.lower()


def test_list_pages_under_construction(client):
    under_construction = []

    for route in get_testable_routes():
        response = client.get(route, follow_redirects=True)
        if response.status_code != 200:
            continue

        body = response.data.decode("utf-8", errors="ignore").lower()
        if "page is under construction" in body:
            under_construction.append(route)

    if under_construction:
        pytest.fail(
            "Pages under construction:\n- " + "\n- ".join(sorted(under_construction))
        )
