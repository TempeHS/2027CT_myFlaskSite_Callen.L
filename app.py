import os
from flask import Flask, render_template, url_for, request, redirect
from werkzeug.exceptions import NotFound
from search_service import (
    sanitize_search_query,
    find_exact_match_endpoint,
    find_partial_matches,
)
from routes.brawlers import brawlers_bp
from routes.gamemodes import gamemodes_bp
from routes.error_handling import errors_bp
from routes.main_pages import main_bp

app = Flask(__name__)
app.register_blueprint(brawlers_bp)
app.register_blueprint(gamemodes_bp)
app.register_blueprint(errors_bp)
app.register_blueprint(main_bp)


# Primary Pages Route
@app.route("/")
def home():
    return render_template("index.html")


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


if __name__ == "__main__":
    host = os.getenv("FLASK_RUN_HOST", "127.0.0.1")
    port = int(os.getenv("FLASK_RUN_PORT", "5000"))
    debug = os.getenv("FLASK_DEBUG", "0") == "1"
    app.run(host=host, port=port, debug=debug)
