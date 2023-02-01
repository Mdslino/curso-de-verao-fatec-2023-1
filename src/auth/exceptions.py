from werkzeug.exceptions import Unauthorized


class UserPasswordException(Unauthorized):
    pass
