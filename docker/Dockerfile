FROM python:3.9-slim

WORKDIR /usr/src/my_service

COPY Pipfile* ./
COPY app ./app/
COPY .env ./
RUN python -m pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --system

EXPOSE 5001

CMD ["waitress-serve", "--port=5001", "--call", "app:create_app"]
