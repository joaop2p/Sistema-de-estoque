from .database import Conect, Users


class Auth(Conect):
    def __init__(self):
        super().__init__()
        
    def _checkUser(self, login: str) -> Users | None:
        result: Users = self.select(Users, method="one", login = login)
        return result

    def _checkPassword(self, user: Users, password: str) -> bool:
        return password == user.password

    def sign_in(self, login: str, password: str) -> bool:
        user = self._checkUser(login)
        if user is not None:
            return self._checkPassword(user, password)
        return False
        

# a = Auth()
# print(a.Login("jpxns2", "10200383"))