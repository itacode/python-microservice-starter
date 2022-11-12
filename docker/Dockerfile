FROM python:3.9

WORKDIR /usr/src/my_service

COPY app app/
COPY server.py .
COPY .env .
COPY pyproject.toml .
COPY poetry.lock .
RUN python -m pip install --upgrade pip
RUN pip install poetry==1.2
RUN poetry install

EXPOSE 5001

CMD poetry run python server.py
