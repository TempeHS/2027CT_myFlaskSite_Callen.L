import re
from flask import Flask, render_template, url_for, request

app = Flask(__name__)


# Primary Pages Route
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


# Footer Pages Route
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


# Search Website
MAX_SEARCH_QUERY_LEN = 80
DISALLOWED_SEARCH_CHARS = re.compile(r"[^a-zA-Z0-9\s_\-']")


def sanitize_search_query(raw_query: str) -> str:
    query = (raw_query or "").strip()[:MAX_SEARCH_QUERY_LEN]
    query = DISALLOWED_SEARCH_CHARS.sub("", query)
    return " ".join(query.split())


SEARCH_PAGES = [
    {
        "title": "Home",
        "endpoint": "home",
        "description": "Main landing page.",
        "keywords": ["index", "main", "start"],
    },
    {
        "title": "Contact",
        "endpoint": "contact",
        "description": "How to contact us.",
        "keywords": ["email", "message", "help"],
    },
    {
        "title": "About",
        "endpoint": "about",
        "description": "About this website.",
        "keywords": ["info", "company", "team"],
    },
    {
        "title": "Privacy",
        "endpoint": "privacy",
        "description": "Privacy policy details.",
        "keywords": ["policy", "data", "security"],
    },
    {
        "title": "Support",
        "endpoint": "support",
        "description": "Support and assistance.",
        "keywords": ["help", "faq", "assist"],
    },
    {
        "title": "Sitemap",
        "endpoint": "sitemap_page",
        "description": "Website page map.",
        "keywords": ["pages", "map", "navigation"],
    },
    {
        "title": "Attribution",
        "endpoint": "attribution",
        "description": "Credits and attributions.",
        "keywords": ["credits", "sources", "license"],
    },
]


@app.route("/search")
def search():
    query = sanitize_search_query(request.args.get("q", "", type=str))
    results = []

    if query:
        q = query.lower()
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
