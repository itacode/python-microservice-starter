FROM python:3.9

RUN apt-get update && apt-get upgrade -y
RUN python -m pip install --upgrade pip

WORKDIR /usr/src/my_service

COPY app app/
COPY server.py .
COPY .env .
COPY pyproject.toml .
COPY poetry.lock .
RUN pip install poetry==1.3
RUN poetry install

EXPOSE 5001

CMD poetry run python server.py
