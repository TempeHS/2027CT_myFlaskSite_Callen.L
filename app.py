import re
from flask import Flask, render_template, url_for, request, redirect, abort

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


# Searching Website
MAX_SEARCH_QUERY_LEN = 80
DISALLOWED_SEARCH_CHARS = re.compile(r"[^a-zA-Z0-9\s_\-']")


def sanitize_search_query(raw_query: str) -> str:
    query = (raw_query or "").strip()[:MAX_SEARCH_QUERY_LEN]
    query = DISALLOWED_SEARCH_CHARS.sub("", query)
    return " ".join(query.split())


SEARCH_PAGES = [
    {
        "title": "🏡 Home",
        "endpoint": "home",
        "description": "The homepage of Brawlable!",
        "keywords": ["index", "main", "start"],
    },
    {
        "title": "📧 Contact",
        "endpoint": "contact",
        "description": "How to contact us.",
        "keywords": ["email", "message", "help"],
    },
    {
        "title": "💁 About",
        "endpoint": "about",
        "description": "About this website.",
        "keywords": ["info", "company", "team"],
    },
    {
        "title": "🔒 Privacy",
        "endpoint": "privacy",
        "description": "Privacy policy details.",
        "keywords": ["policy", "data", "security"],
    },
    {
        "title": "📧 Support",
        "endpoint": "support",
        "description": "Support and assistance.",
        "keywords": ["help", "faq", "assist"],
    },
    {
        "title": "🗺️ Sitemap",
        "endpoint": "sitemap_page",
        "description": "Website page map.",
        "keywords": ["pages", "map", "navigation"],
    },
    {
        "title": "✍️ Attribution",
        "endpoint": "attribution",
        "description": "Credits and attributions.",
        "keywords": ["credits", "sources", "license"],
    },
    # Brawler Pages
    {
        "title": "🥊 Brawlers",
        "endpoint": "brawlers",
        "description": "All brawlers in Brawl Stars.",
        "keywords": ["characters", "heroes", "fighters"],
    },
    {
        "title": "🟢 Rare Brawlers",
        "endpoint": "rare",
        "description": "Rare rarity brawlers.",
        "keywords": ["brawlers", "rare", "rarity"],
    },
    {
        "title": "🔵 Super Rare Brawlers",
        "endpoint": "super_rare",
        "description": "Super Rare rarity brawlers.",
        "keywords": ["brawlers", "super rare", "rarity"],
    },
    {
        "title": "🟣 Epic Brawlers",
        "endpoint": "epic",
        "description": "Epic rarity brawlers.",
        "keywords": ["brawlers", "epic", "rarity"],
    },
    {
        "title": "🔴 Mythic Brawlers",
        "endpoint": "mythic",
        "description": "Mythic rarity brawlers.",
        "keywords": ["brawlers", "mythic", "rarity"],
    },
    {
        "title": "🟡 Legendary Brawlers",
        "endpoint": "legendary",
        "description": "Legendary rarity brawlers.",
        "keywords": ["brawlers", "legendary", "rarity"],
    },
    {
        "title": "👑 Ultra Legendary Brawlers",
        "endpoint": "ultra_legendary",
        "description": "Ultra Legendary rarity brawlers.",
        "keywords": ["brawlers", "ultra legendary", "rarity"],
    },
    # Gamemode Pages
    {
        "title": "⭐️ Bounty",
        "endpoint": "bounty",
        "description": "Bounty game mode.",
        "keywords": ["gamemode", "stars", "kills"],
    },
    {
        "title": "⚽️ Brawl Ball",
        "endpoint": "brawl_ball",
        "description": "Brawl Ball game mode.",
        "keywords": ["gamemode", "3v3", "5v5", "ball"],
    },
    {
        "title": "💎 Gem Grab",
        "endpoint": "gem_grab",
        "description": "Gem Grab game mode.",
        "keywords": ["gamemode", "gems", "grab", "3v3"],
    },
    {
        "title": "💰 Heist",
        "endpoint": "heist",
        "description": "Heist game mode.",
        "keywords": ["gamemode", "safe", "3v3"],
    },
    {
        "title": "⭕️ Hot Zone",
        "endpoint": "hot_zone",
        "description": "Hot Zone game mode.",
        "keywords": ["gamemode", "zone", "3v3"],
    },
    {
        "title": "🧙‍♂️ Showdown",
        "endpoint": "showdown",
        "description": "Showdown game mode.",
        "keywords": ["gamemode", "solo", "duo", "trio"],
    },
    {
        "title": "🔫 Knockout",
        "endpoint": "knockout",
        "description": "Knockout game mode.",
        "keywords": ["gamemode", "3v3", "team", "5v5"],
    },
    {
        "title": "👥 Wipeout",
        "endpoint": "wipeout",
        "description": "Wipeout game mode.",
        "keywords": ["gamemode", "team", "5v5"],
    },
]


@app.route("/search")
def search():
    query = sanitize_search_query(request.args.get("q", "", type=str))
    results = []

    if query:
        q = query.lower()
        for page in SEARCH_PAGES:
            if q == page["title"].lower() or q == page["endpoint"].lower():
                return redirect(url_for(page["endpoint"]))

        for page in SEARCH_PAGES:
            searchable_text = " ".join(
                [page["title"], page["description"], " ".join(page["keywords"])]
            ).lower()

            if q in searchable_text:
                results.append(
                    {
                        "title": page["title"],
                        "description": page["description"],
                        "url": url_for(page["endpoint"]),
                    }
                )

    return render_template("search.html", query=query, results=results)


# 404 Page Route
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
