from flask_login import UserMixin


class User(UserMixin):

    def __init__(self, id, username):
        self.id = id
        self.username = username


users = {
    "admin": {
        "password": "auditforge123"
    }
}


def get_user(username):

    if username in users:
        return User(username, username)

    return None


def verify_login(username, password):

    if username not in users:
        return False

    return users[username]["password"] == password