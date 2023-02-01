from uuid import uuid4

from sqlalchemy.dialects.postgresql import UUID
from werkzeug.security import check_password_hash, generate_password_hash

from src.auth.exceptions import UserPasswordException
from src.ext.database import TimestampedModel, db


class User(TimestampedModel):
    id = db.Column(db.BigInteger, primary_key=True)
    external_id = db.Column(
        UUID(as_uuid=True),
        unique=True,
        default=uuid4,
        server_default=db.func.uuid_generate_v4(),
    )
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    is_active = db.Column(db.Boolean, default=True, nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"

    def __str__(self):
        return self.username

    @property
    def is_authenticated(self):
        return True

    def get_id(self):
        return self.external_id

    def check_password(self, password):
        if check_password_hash(self.password, password):
            return True
        raise UserPasswordException("Senha inválida")

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def authenticate(self, password):
        return self.check_password(password) and self.is_active


class Group(TimestampedModel):
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String, nullable=True)

    def __repr__(self):
        return f"<Group {self.name}>"

    def __str__(self):
        return self.name


class Action(TimestampedModel):
    name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String, nullable=True)

    def __repr__(self):
        return f"<Action {self.name}>"

    def __str__(self):
        return self.name


class GroupAction(TimestampedModel):
    group_id = db.Column(
        db.BigInteger, db.ForeignKey("group.id"), nullable=False
    )
    action_id = db.Column(
        db.BigInteger, db.ForeignKey("action.id"), nullable=False
    )
    group = db.relationship("Group", backref="group_actions")
    action = db.relationship("Action", backref="group_actions")

    def __repr__(self):
        return f"<GroupAction {self.group.name} {self.action.name}>"

    def __str__(self):
        return f"{self.group.name} {self.action.name}"


class UserGroup(TimestampedModel):
    user_id = db.Column(
        db.BigInteger, db.ForeignKey("user.id"), nullable=False
    )
    group_id = db.Column(
        db.BigInteger, db.ForeignKey("group.id"), nullable=False
    )
    user = db.relationship("User", backref="user_groups")
    group = db.relationship("Group", backref="user_groups")

    def __repr__(self):
        return f"<UserGroup {self.user.username} {self.group.name}>"

    def __str__(self):
        return f"{self.user.username} {self.group.name}"
