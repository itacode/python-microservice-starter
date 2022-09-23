from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    id: Optional[int] = None
    username: Optional[str] = None
    email: Optional[str] = None
    is_deleted: Optional[bool] = None
    create_time: Optional[str] = None
    update_time: Optional[str] = None
