from flask import Blueprint, render_template

gamemodes_bp = Blueprint("gamemodes", __name__, url_prefix="/gamemodes")


@gamemodes_bp.route("/bounty", endpoint="bounty")
def bounty():
    return render_template("gamemodes/bounty.html")


@gamemodes_bp.route("/brawl-ball", endpoint="brawl_ball")
def brawl_ball():
    return render_template("gamemodes/brawl-ball.html")


@gamemodes_bp.route("/gem-grab", endpoint="gem_grab")
def gem_grab():
    return render_template("gamemodes/gem-grab.html")


@gamemodes_bp.route("/heist", endpoint="heist")
def heist():
    return render_template("gamemodes/heist.html")


@gamemodes_bp.route("/hot-zone", endpoint="hot_zone")
def hot_zone():
    return render_template("gamemodes/hot-zone.html")


@gamemodes_bp.route("/showdown", endpoint="showdown")
def showdown():
    return render_template("gamemodes/showdown.html")


@gamemodes_bp.route("/knockout", endpoint="knockout")
def knockout():
    return render_template("gamemodes/knockout.html")


@gamemodes_bp.route("/wipeout", endpoint="wipeout")
def wipeout():
    return render_template("gamemodes/wipeout.html")
