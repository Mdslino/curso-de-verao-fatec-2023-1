import logging

from flask import flash, redirect, render_template, request, url_for
from flask_login import login_user, logout_user

from src.auth.forms import LoginForm, SignupForm
from src.auth.models import User

logger = logging.getLogger(__name__)


def login():
    form = LoginForm()
    if request.method == "POST":
        if form.validate_on_submit() and (
            user := User.query.filter_by(username=form.username.data).first()
        ):
            if user.authenticate(form.password.data):
                login_user(user)
                logger.info(f"User {user.username} logged in.")
                flash("Login realizado com sucesso.", "success")
                return redirect(url_for("webui.index"))
            logger.warning(f"User {user.username} failed to login.")
            flash("Usuário ou senha inválidos.", "danger")

    logger.info("Redirecting to login page.")
    return render_template(
        "auth/auth.html", form=form, title="Entrar", flow="Cadastrar"
    )


def logout():
    logout_user()
    flash("Logout realizado com sucesso.", "success")
    logger.info("User logged out.")
    return redirect(url_for("webui.index"))


def signup():
    form = SignupForm()
    if request.method == "POST":
        if form.validate_on_submit():
            user = User(username=form.username.data)
            user.set_password(form.password.data)
            user.save()
            logger.info(f"User {user.username} created.")
            flash("Cadastro realizado com sucesso.", "success")
            return redirect(url_for("webui.index"))

    logger.info("Redirecting to signup page.")
    return render_template(
        "auth/auth.html", form=form, title="Cadastrar", flow="Cadastrar"
    )
