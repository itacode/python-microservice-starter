# Python microservice starter
A boilerplate to start developing microservices.

## Features
- Web framework [Connexion](https://connexion.readthedocs.io/en/latest/index.html) on top of Flask that automagically validates and handles HTTP requests defined using [OpenAPI](https://www.openapis.org/)
- Development server [Flask](https://flask.palletsprojects.com/en/2.0.x/) with live reload
- Production server [Waitress](https://docs.pylonsproject.org/projects/waitress/en/latest/)
- API `app/api/openapi/api.oas.yml` designed following [OpenAPI Specification](https://swagger.io/specification/)
- Interactive API documentation (Swagger UI) [http://localhost:5001/api/v1/my_service/ui](http://localhost:5001/api/v1/my_service/ui)
- Environment variables file `.env` for the app configuration
- Docker `docker-compose.yml` and `docker/Dockerfile` to run the prodution server
- Openapi generator [openapi-generator-cli](https://github.com/OpenAPITools/openapi-generator-cli) configured to generate clients
- MySQL database with docker compose
- ORM [SQLAlchemy](https://www.sqlalchemy.org/)
- Tool [sqlacodegen](https://github.com/agronholm/sqlacodegen) that reads the structure of an existing database and generates the appropriate SQLAlchemy model code
- Data validator [Pydantic](https://pydantic-docs.helpmanual.io/)
- Unit test framework [pytest](https://docs.pytest.org/en/7.1.x/contents.html)
- Linter [Flake8](https://flake8.pycqa.org/en/latest/)
- Code formatter [Black](https://black.readthedocs.io/en/stable/)
- Static type checker [Mypy](http://mypy-lang.org/)

## Installation
Visual Studio Code is the recommended editor, please install the recommended extensions in `.vscode/extensions.json`.

Install [poetry](https://python-poetry.org/docs/#installation).

Install required packages:
```shell
poetry install --dev
```

## Development
Start the development server with automatic reload:
```shell
poetry shell
flask run
```

### Run database Docker
Run:
```shell
cd db
docker compose up -d --build
```
Stop:
```shell
cd db
docker compose down
```

### Unit test
```shell
poetry shell
pytest
```

### OpenAPI generator
In `openapi-generator` install the required packages:
```shell
npm install
```
Generate clients:
```shell
npm run generate
```

## Server Docker
In the project root there is the `docker-compose.yml`.

Run:
```shell
docker compose up -d --build
```
Stop:
```shell
docker compose down
```

## Production server
```shell
poetry run python server.py
```
