import os
from ...utils.singleton import SingletonMeta


class User(metaclass = SingletonMeta):
    _path = r"assets\images\profile"
    _files = os.listdir(_path)
    
    def __init__(self) -> None:
        self._login = "@Teste"
        self._profile_photo = self._files[0] if len(self._files) > 0 else None
        self._email = "teste@exemple.com"
        self._name = "Guess"
        self._password = "teste@123"

    def setPassword(self, password: str) -> None:
        self._password = password

    def setLogin(self, login):
        self._login = login
        
    def setName(self, username):
        self._name = username

    def setProfilePhoto(self, photo) -> None:
        self._profile_photo = photo

    def setEmail(self, email) -> None:
        self._email = email

    def getPassword(self) -> str:
        return self._password

    def getLogin(self) -> str:
        return self._login

    def getName(self) -> str:
        return self._name

    def getProfilePhoto(self) -> str:
        return os.path.realpath(os.path.join(self._path, self._profile_photo))

    def getEmail(self) -> str:
        return self._email

    def __str__(self):
        return f"User(login: {self.getLogin()}, email: {self.getEmail()}, name: {self.getName()})"

    def destroy(self) -> None:
        self.__init__()
