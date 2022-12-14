from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import DBConfig

engine = create_engine(DBConfig.MY_SERVICE_DB_URL, future=True)

# https://docs.sqlalchemy.org/en/14/orm/session_basics.html#using-a-sessionmaker
db_session = sessionmaker(bind=engine, expire_on_commit=False)
