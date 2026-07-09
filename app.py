from flask import Flask, render_template, url_for, request, redirect
from werkzeug.exceptions import NotFound
from search_service import (
    sanitize_search_query,
    find_exact_match_endpoint,
    find_partial_matches,
)
from routes.brawlers import brawlers_bp
from routes.gamemodes import gamemodes_bp

app = Flask(__name__)
app.register_blueprint(brawlers_bp)
app.register_blueprint(gamemodes_bp)


app = Flask(__name__)


# Primary Pages Route
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


# More Primary Pages Route
@app.route("/about")
def about():
    return render_template("pages/about.html")


@app.route("/privacy")
def privacy():
    return render_template("pages/privacy.html")


@app.route("/support")
def support():
    return render_template("pages/support.html")


@app.route("/sitemap")
def sitemap_page():
    return render_template("pages/sitemap.html")


@app.route("/attribution")
def attribution():
    return render_template("pages/attribution.html")


# Brawler Pages
@app.route("/brawlers")
def brawlers():
    return render_template("brawlers.html")


@app.route("/brawlers/rare")
def rare():
    return render_template("brawlers/rare.html")


@app.route("/brawlers/super-rare")
def super_rare():
    return render_template("brawlers/super-rare.html")


@app.route("/brawlers/epic")
def epic():
    return render_template("brawlers/epic.html")


@app.route("/brawlers/mythic")
def mythic():
    return render_template("brawlers/mythic.html")


@app.route("/brawlers/legendary")
def legendary():
    return render_template("brawlers/legendary.html")


@app.route("/brawlers/ultra-legendary")
def ultra_legendary():
    return render_template("brawlers/ultra-legendary.html")


# Gamemode Pages
@app.route("/gamemodes/bounty")
def bounty():
    return render_template("gamemodes/bounty.html")


@app.route("/gamemodes/brawl-ball")
def brawl_ball():
    return render_template("gamemodes/brawl-ball.html")


@app.route("/gamemodes/gem-grab")
def gem_grab():
    return render_template("gamemodes/gem-grab.html")


@app.route("/gamemodes/heist")
def heist():
    return render_template("gamemodes/heist.html")


@app.route("/gamemodes/hot-zone")
def hot_zone():
    return render_template("gamemodes/hot-zone.html")


@app.route("/gamemodes/showdown")
def showdown():
    return render_template("gamemodes/showdown.html")


@app.route("/gamemodes/knockout")
def knockout():
    return render_template("gamemodes/knockout.html")


@app.route("/gamemodes/wipeout")
def wipeout():
    return render_template("gamemodes/wipeout.html")


# Searching Website
@app.route("/search")
def search():
    query = sanitize_search_query(request.args.get("q", "", type=str))
    results = []

    if query:
        endpoint = find_exact_match_endpoint(query)
        if endpoint:
            return redirect(url_for(endpoint))

        for page in find_partial_matches(query):
            results.append(
                {
                    "title": page["title"],
                    "description": page["description"],
                    "url": url_for(page["endpoint"]),
                }
            )

    return render_template("search.html", query=query, results=results)


@app.errorhandler(404)
def handle_404(e):
    error_reason = "PAGE_NOT_FOUND"
    if e.description and not e.description.startswith("The requested URL"):
        error_reason = e.description.upper().replace(" ", "_")
    else:
        try:
            adapter = app.create_url_map().bind_to_environ(request.environ)
            adapter.match()
        except NotFound as routing_error:
            if "not found" not in str(routing_error).lower():
                error_reason = "INVALID_ROUTE_PARAMETER"
        except Exception:
            error_reason = "ROUTING_ENGINE_FAILED"
        return (
            render_template("404.html", error_code=error_reason, site_url=request.url),
            404,
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
