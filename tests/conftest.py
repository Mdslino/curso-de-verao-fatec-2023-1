import pytest
from sqlalchemy_utils import create_database, database_exists, drop_database

from src.app import create_app, minimal_app
from src.ext.database import db
from tests.factory import UserFactory


@pytest.fixture(scope="session")
def min_app():
    app = minimal_app()
    return app


@pytest.fixture(scope="session", autouse=True)
def app():
    app = create_app()
    with app.app_context():
        SQLALCHEMY_DATABASE_URI = app.config["SQLALCHEMY_DATABASE_URI"]
        if not database_exists(SQLALCHEMY_DATABASE_URI):
            create_database(SQLALCHEMY_DATABASE_URI)
        db.session.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp"')
        db.session.commit()
        db.create_all(app=app)
        yield app
        db.session.close_all()
        db.drop_all(app=app)


@pytest.fixture
def auth_user():
    return UserFactory()
