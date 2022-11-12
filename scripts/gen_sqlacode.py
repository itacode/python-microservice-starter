import subprocess
import sys

from app.config import DBConfig

command = f"sqlacodegen {DBConfig.MY_SERVICE_DB_URL} --noinflect --outfile app/entities/orm/orm_model.py"


def gen_sqlacode():
    subprocess.run(command)


def main():
    gen_sqlacode()


if __name__ == "__main__":
    sys.exit(main())
