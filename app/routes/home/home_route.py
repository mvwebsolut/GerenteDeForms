from flask import Blueprint, request, render_template
from datetime import datetime

home_route = Blueprint("home", __name__, url_prefix="/")

@home_route.route("/", methods=["GET"])
def index():
    return render_template("index.html")

