from dataclasses import dataclass
from typing import Iterable

from sqlalchemy import select

import app.entities.orm.orm_model as orm
from app.database import session_scope
from app.entities.user import User


class UsersService:
    @dataclass
    class FindResult:
        users: list[User]

    def find(self) -> FindResult:
        with session_scope() as session:
            stmt = select(orm.User).where(orm.User.is_deleted == 0)
            orm_users: Iterable[orm.User] = session.scalars(stmt)

            users: list[User] = []
            for orm_user in orm_users:
                users.append(User(
                    id=orm_user.id,
                    email=orm_user.email,
                    username=orm_user.username,
                    is_deleted=bool(orm_user.is_deleted),
                    create_time=orm_user.create_time,
                    update_time=orm_user.update_time
                ))

        return self.FindResult(users=users)
