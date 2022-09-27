from app.api.service.users_service import UsersService

_users_service = UsersService()


def get_users():
    users = _users_service.find()
    return users.dict()
