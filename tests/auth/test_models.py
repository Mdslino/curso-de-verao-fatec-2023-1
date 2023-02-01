from src.auth.models import User
from src.ext.database import db


def test_user_exist(auth_user):
    query = db.select(User)
    user = db.session.execute(query).scalar_one()

    assert auth_user.id == user.id
    assert user.check_password("my_password")
    assert user.authenticate("my_password")
