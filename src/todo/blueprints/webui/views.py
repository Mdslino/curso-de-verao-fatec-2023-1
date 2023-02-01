import logging

from flask import flash, redirect, render_template, request, url_for

from src.todo.forms import TodoForm
from src.todo.models import Todo

logger = logging.getLogger(__name__)


def todos():
    form = TodoForm()
    if request.method == "POST":
        if form.validate_on_submit():
            todo = Todo()
            form.populate_obj(todo)
            todo.save()
            logger.info(f"Todo {todo.title} created.")
            flash("Todo criado com sucesso.", "success")
            return redirect(url_for("todo.todos"))
    return render_template("todo/todos.html", form=form)


def todos_items():
    todos = Todo.query.all()
    return render_template("todo/todo-item.html", todos=todos)
