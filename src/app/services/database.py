from typing import Literal, Optional
import sqlalchemy
from sqlmodel import Field, SQLModel, create_engine, Session, select

from ...utils.singleton import SingletonMeta

class Conect(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self.engine = create_engine("mysql+pymysql://root:@127.0.0.1:3306/sistema_storage")
        SQLModel.metadata.create_all(self.engine)

    def select(self, table: SQLModel, method: Literal["all", "one"] = "all", **kwargs) -> list:
        try:
            with Session(self.engine) as session:
                statement = select(table)
                for key, value in kwargs.items():
                    column = getattr(table, key)
                    statement = statement.where(column == value)
                return session.exec(statement).all() if method == "all" else session.exec(statement).first()
        except sqlalchemy.exc.SQLAlchemyError:
            return []

class Users(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    login: str 
    password: str
    email: str
    name: str

    # TODO criar uma tabela de log com os eventos de acesso à aplicação
    # TODO criar um código token para validação

