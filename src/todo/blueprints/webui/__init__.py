from flask import Blueprint

from src.todo.blueprints.webui.views import todos, todos_items

bp = Blueprint(
    "todo", __name__, template_folder="templates", url_prefix="/todo"
)
bp.add_url_rule(
    "", view_func=todos, methods=("GET", "POST"), endpoint="todos"
)
bp.add_url_rule(
    "/todo-item",
    view_func=todos_items,
    methods=("GET",),
    endpoint="todos_items",
)


def init_app(app):
    app.register_blueprint(bp)
