from flask import Flask, render_template

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


# 404 Page Route
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
