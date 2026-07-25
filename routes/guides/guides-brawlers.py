from flask import Blueprint, render_template, abort

brawlers_bp = Blueprint("brawlers", __name__, url_prefix="/brawlers")


@brawlers_bp.route("/rare/<name>")
def rare_brawler_guide(name):

    rare_brawlers = [
        "barley",
        "brock",
        "bull",
        "colt",
        "el-primo",
        "nita",
        "poco",
        "rosa",
    ]

    brawler_id = name.lower()

    if brawler_id in rare_brawlers:
        return render_template(f"brawlers/rare/{brawler_id}.html")
    abort(404)
