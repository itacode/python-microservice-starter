from typing import Iterable, cast

from pydantic import BaseModel
from sqlalchemy import select

import app.entities.orm.orm_model as orm
from app.database import db_session
from app.entities.user import User


class UsersService:
    class FindResult(BaseModel):
        users: list[User]

    def find(self) -> FindResult:
        with db_session.begin() as session:
            stmt = select(orm.User).where(orm.User.is_deleted == 0)
            orm_users = cast(
                Iterable[orm.User], session.scalars(stmt)
            )  # override ScalarResult type

            users: list[User] = []
            for orm_user in orm_users:
                users.append(User.from_orm(orm_user))

        return self.FindResult(users=users)
