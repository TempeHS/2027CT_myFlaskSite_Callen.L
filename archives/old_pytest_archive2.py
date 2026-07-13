import pytest
from app import app, sanitize_search_query, SEARCH_PAGES

# Note: This code has no intentions of being repaired and acts as a reference material now.


@pytest.fixture
def client():
    """Create a test client for our Flask app."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


# ============ OLD HOME PAGE TESTS ============


def test_home_page_loads(client):
    """Test that the home page returns status 200."""
    response = client.get("/")
    assert response.status_code == 200


def test_home_page_has_title(client):
    """Test that the home page contains our site title."""
    response = client.get("/")
    assert b"Brawlable" in response.data


def test_home_page_has_nav(client):
    """Test that the navigation is included."""
    response = client.get("/")
    assert b"navbar" in response.data


def test_home_page_has_bootstrap(client):
    """Test that Bootstrap CSS is linked."""
    response = client.get("/")
    assert b"bootstrap" in response.data


# ============ OLD CONTACT PAGE TESTS ============


def test_contact_page_loads(client):
    """Test that the contact page returns status 200."""
    response = client.get("/contact")
    assert response.status_code == 200


def test_contact_page_has_form(client):
    """Test that the contact page has a form."""
    response = client.get("/contact")
    assert b"<form" in response.data


# ================== TESTS IF ALL WEBPAGES ARE ABLE TO LOAD WITH RETURN CODE 200 ==================
@pytest.fixture
def pages_load_200_OK():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@pytest.mark.parametrize(
    "route",
    [
        # FOR HOMEPAGE
        "/",
        # FOR ITEMS IN PAGES
        "/contact",
        "/about",
        "/privacy",
        "/support",
        "/sitemap",
        "/attribution",
        # FOR BRAWLERS
        "/brawlers",
        "/brawlers/rare",
        "/brawlers/super-rare",
        "/brawlers/epic",
        "/brawlers/mythic",
        "/brawlers/legendary",
        "/brawlers/ultra-legendary",
        # FOR GAMEMODES
        "/gamemodes/bounty",
        "/gamemodes/brawl-ball",
        "/gamemodes/gem-grab",
        "/gamemodes/heist",
        "/gamemodes/hot-zone",
        "/gamemodes/showdown",
        "/gamemodes/knockout",
        "/gamemodes/wipeout",
        # FOR SEARCH TESTING
        "/search",
        "/search?q=gem",
    ],
)
def test_routes_return_200(client, route):
    response = client.get(route)
    assert response.status_code == 200


# ================== TESTS SEARCH BAR REDIRECT FEATURE ==================
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


# ================== TESTS IF 404 PAGE WORKS SUCCESSFULLY ==================
def test_404_page(client):
    response = client.get("/this-page-does-not-exist")
    assert response.status_code == 404


# ================== TEST CODE SANTISATION IN SEARCH QUERY ==================
def test_sansitizing_blank_spaces():
    assert sanitize_search_query("   hello world   ") == "hello world"


def test_sansitizing_special_char():
    assert sanitize_search_query("<script>alert(1)</script>") == "scriptalert1script"


def test_sanitize_limits_length():
    query = "a" * 200
    assert len(sanitize_search_query(query)) == 80


# ================== TEST SEARCH PAGES ==================


def all_search_terms():
    seen = set()

    for page in SEARCH_PAGES:
        yield page["endpoint"]

        if page["title"] not in seen:
            seen.add(page["title"])
            yield page["title"]

        for keyword in page["keywords"]:
            if keyword not in seen:
                seen.add(keyword)
                yield keyword


@pytest.mark.parametrize("term", list(all_search_terms()))
def test_every_search_term(client, term):
    response = client.get(f"/search?q={term}", follow_redirects=True)
    assert response.status_code == 200


# ================== EXPERIMENTAL AUTO ADD OK 200 TESTS ==================


def get_routes():
    routes = []

    for rule in app.url_map.iter_rules():
        # Only test GET routes
        if "GET" not in rule.methods:
            continue

        # Skip Flask's static endpoint
        if rule.endpoint == "static":
            continue

        # Skip routes with URL parameters
        if rule.arguments:
            continue

        routes.append(rule.rule)

    return sorted(routes)


@pytest.mark.parametrize("route", get_routes())
def test_all_get_routes_return_success(client, route):
    response = client.get(route)
    if response.status_code == 302:
        response = client.get(route, follow_redirects=True)

    assert response.status_code == 200


# ================== SECOND SEARCH SANITIZATION AND TEST ==================
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
