from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.BigInteger, primary_key=True)

    def save(self, commit=True):
        db.session.add(self)

        if commit:
            db.session.commit()

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        db.session.commit()


class TimestampedModel(BaseModel):
    __abstract__ = True

    created_at = db.Column(
        db.DateTime, default=datetime.now, server_default=db.func.now()
    )
    updated_at = db.Column(
        db.DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        server_default=db.func.now(),
        server_onupdate=db.func.now(),
    )


def init_app(app):
    db.init_app(app)
