import base64
from datetime import datetime
from typing import Literal, Optional

class Client:
    _id: int | None
    _name: str
    _email: str
    _phone: Optional[str]
    _tag: int = 0
    _created_at: Optional[datetime]
    _updated_at: Optional[datetime]
    _photo: Optional[bytes]
    _status: int = 0

    def __init__(self, id: Optional[int], name: str, email: str, phone: Optional[str], tag: int, created_at: Optional[datetime], updated_at: Optional[datetime], photo: Optional[bytes], status: int) -> None:
        self._id = id
        self._name = name
        self._email = email
        self._phone = phone
        self._tag = tag
        self._status = status
        self._created_at = created_at
        self._updated_at = updated_at
        self._photo = photo

    @staticmethod
    def from_dict(data: dict) -> "Client":
        return Client(
            id=data.get("id"),
            name=data.get("name", 'Guest'),
            email=data.get("email", 'guest@example.com'),
            phone=data.get("phone"),
            tag=data.get("tag", 0),
            created_at=datetime.fromisoformat(data["created_at"]) if data.get("created_at") else None,
            updated_at=datetime.fromisoformat(data["updated_at"]) if data.get("updated_at") else None,
            photo=base64.b64decode(data["photo"]) if data.get("photo") else None,
            # photo=base64.b64decode(data["photo"]) if data.get("photo") else None,
            status=data.get("status", 0)
        )

    # Getters
    @property
    def id(self) -> Optional[int]:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def email(self) -> str:
        return self._email

    @property
    def tag(self) -> Literal['Active', 'Inactive', 'Pending']:
        options = ['Active', 'Inactive', 'Pending'] 
        return options[self._tag] # type: ignore

    @property
    def created_at(self) -> Optional[datetime]:
        return self._created_at

    @property
    def updated_at(self) -> Optional[datetime]:
        return self._updated_at

    @property
    def photo(self) -> Optional[bytes]:
        return self._photo

    @property
    def status(self) -> Literal['online', 'offline', 'away']:
        options = ['online', 'offline', 'away']
        return options[self._status] # type: ignore