from src.ext.database import TimestampedModel, db


class Todo(TimestampedModel):
    id = db.Column(db.BigInteger, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    is_done = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return f"<Todo {self.title}>"

    def __str__(self):
        return self.title
