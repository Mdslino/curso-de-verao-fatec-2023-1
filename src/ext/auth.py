from flask_login import LoginManager

from src.auth.models import User

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(external_id=user_id).first()


def init_app(app):
    login_manager.init_app(app)
