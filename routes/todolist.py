from flask import Blueprint

todolist = Blueprint("todolist", __name__)


@todolist.route("/")
def home():
    return "my todolist!!"
