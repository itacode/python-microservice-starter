import os

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

from app.config import DBConfig

connection_url = DBConfig.MY_SERVICE_DB_URL
data_directory = os.path.join(os.path.dirname(__file__), "data")


class DataHelper:
    """Helper to manage test data im the database"""

    def __init__(self, connection_url: str = connection_url, data_directory: str = data_directory) -> None:
        self.engine: Engine = create_engine(connection_url)
        self.data_base_dir = data_directory

    def insert_from_csv(self, table_name: str, subdir_file_path: str, sep=",", quotechar='"', encoding="utf8"):
        """Insert in a table the data read from a CSV file in a sudirectory of test data directory"""
        file_path = os.path.join(self.data_base_dir, subdir_file_path)
        df = pd.read_csv(filepath_or_buffer=file_path, sep=sep,
                         quotechar=quotechar, encoding=encoding)
        df.to_sql(table_name, con=self.engine, index=False, if_exists="append")

    def truncate_table(self, table_name: str):
        con = self.engine.connect()
        con.execute(f"TRUNCATE TABLE {table_name}")
        con.close()

    def delete_rows(self, table_name: str, ids: list[int]):
        ids_joined = ",".join([str(i) for i in ids])
        con = self.engine.connect()
        con.execute(f"DELETE FROM {table_name} WHERE id in ({ids_joined})")
        con.close()

    def delete_all_rows(self, table_name: str):
        con = self.engine.connect()
        con.execute(f"DELETE FROM {table_name}")
        con.close()
