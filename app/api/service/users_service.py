from typing import Iterable

from pydantic import BaseModel
from sqlalchemy import select

import app.entities.orm.orm_model as orm
from app.database import Session
from app.entities.user import User


class UsersService:
    class FindResult(BaseModel):
        users: list[User]

    def find(self) -> FindResult:
        with Session.begin() as session:
            stmt = select(orm.User).where(orm.User.is_deleted == 0)
            orm_users: Iterable[orm.User] = session.scalars(stmt)

            users: list[User] = []
            for orm_user in orm_users:
                users.append(User.from_orm(orm_user))

        return self.FindResult(users=users)
