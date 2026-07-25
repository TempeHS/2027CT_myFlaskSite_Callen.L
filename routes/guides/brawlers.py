from flask import Blueprint, render_template, abort

brawlers_bp = Blueprint("brawlers", __name__, url_prefix="/brawlers")


@brawlers_bp.route("", endpoint="brawlers")
def brawlers():
    return render_template("brawlers.html")


@brawlers_bp.route("/rare", endpoint="rare")
def rare():
    return render_template("brawlers/rare.html")


@brawlers_bp.route("/super-rare", endpoint="super_rare")
def super_rare():
    return render_template("brawlers/super-rare.html")


@brawlers_bp.route("/epic", endpoint="epic")
def epic():
    return render_template("brawlers/epic.html")


@brawlers_bp.route("/mythic", endpoint="mythic")
def mythic():
    return render_template("brawlers/mythic.html")


@brawlers_bp.route("/legendary", endpoint="legendary")
def legendary():
    return render_template("brawlers/legendary.html")


@brawlers_bp.route("/ultra-legendary", endpoint="ultra_legendary")
def ultra_legendary():
    return render_template("brawlers/ultra-legendary.html")
