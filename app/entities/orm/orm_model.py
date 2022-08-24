# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, String, text
from sqlalchemy.dialects.mysql import DATETIME, TINYINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, unique=True)
    username = Column(String(16, 'utf8mb4_bin'), nullable=False)
    email = Column(String(255, 'utf8mb4_bin'), nullable=False)
    is_deleted = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    create_time = Column(DATETIME(fsp=6), nullable=False, server_default=text("CURRENT_TIMESTAMP(6)"))
    update_time = Column(DATETIME(fsp=6), nullable=False, server_default=text("CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6)"))


class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True, unique=True)
    content = Column(String(255, 'utf8mb4_bin'), nullable=False)
    user_id = Column(ForeignKey('user.id'), nullable=False, index=True)
    is_deleted = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    create_time = Column(DATETIME(fsp=6), nullable=False, server_default=text("CURRENT_TIMESTAMP(6)"))
    update_time = Column(DATETIME(fsp=6), nullable=False, server_default=text("CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6)"))

    user = relationship('User')
