from flask import Blueprint, render_template

todolist = Blueprint("todolist", __name__)


@todolist.route("/")
def home():
    return render_template("home.html")


@todolist.route("/main")
def main():
    return render_template("todolist/home.html")
