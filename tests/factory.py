from factory.alchemy import SQLAlchemyModelFactory
from werkzeug.security import generate_password_hash

from src.auth.models import User
from src.ext.database import db


class UserFactory(SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = db.session

    username = "my_user"
    password = generate_password_hash("my_password")
