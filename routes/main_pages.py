from flask import Blueprint, render_template

main_bp = Blueprint("main", __name__, url_prefix="/")


@main_bp.route("/contact")
def contact():
    return render_template("contact.html")


@main_bp.route("/onboarding")
def onboarding():
    return render_template("onboarding.html")


@main_bp.route("/brawlers")
def brawlers():
    return render_template("brawlers.html")


# More Primary Pages Route
@main_bp.route("/about")
def about():
    return render_template("pages/about.html")


@main_bp.route("/privacy")
def privacy():
    return render_template("pages/privacy.html")


@main_bp.route("/support")
def support():
    return render_template("pages/support.html")


@main_bp.route("/sitemap")
def sitemap_page():
    return render_template("pages/sitemap.html")


@main_bp.route("/attribution")
def attribution():
    return render_template("pages/attribution.html")
