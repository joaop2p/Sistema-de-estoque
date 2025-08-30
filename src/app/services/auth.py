from ..models.user import User
from .database import Conect, Users


class Auth():
    def __init__(self):
        self.conect = Conect()
        
    def _checkUser(self, login: str, password: str) -> Users | None:
        result: Users = self.conect.select(Users, method="one", login = login, password = password)
        return result

    def _checkPassword(self, user: Users, password: str) -> bool:
        return password == user.password
    
    def _createUser(self, user: Users) -> Users:
        new_user = User()
        new_user.setLogin(user.login)
        new_user.setEmail(user.email)
        new_user.setName(user.name)
        new_user.setPassword(user.password)


    def sign_in(self, login: str, password: str) -> bool:
        user = self._checkUser(login)
        if user is not None:
            return self._checkPassword(user, password)
        return False

