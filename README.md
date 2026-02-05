# Python microservice starter

A boilerplate to start developing microservices.

## Features

- Web framework [Connexion](https://connexion.readthedocs.io/en/latest/index.html) on top of Flask that automagically validates and handles HTTP requests defined using [OpenAPI](https://www.openapis.org/)
- Production ASGI web server [Uvicorn](https://www.uvicorn.org/)
- Development server with reload
- API `app/api/openapi/api.oas.yml` designed following [OpenAPI Specification](https://swagger.io/specification/)
- Interactive API documentation (Swagger UI) [http://localhost:8000/api/v1/my_service/ui](http://localhost:8000/api/v1/my_service/ui)
- Environment variables file `.env` for the app configuration
- Docker `docker-compose.yml` and `docker/Dockerfile` to run the prodution server
- Openapi generator [openapi-generator-cli](https://github.com/OpenAPITools/openapi-generator-cli) configured to generate clients
- MySQL database with docker compose
- ORM [SQLAlchemy](https://www.sqlalchemy.org/)
- Data validator [Pydantic](https://pydantic-docs.helpmanual.io/)
- Unit test framework [pytest](https://docs.pytest.org/en/7.1.x/contents.html)

## Installation

Visual Studio Code is the recommended editor, please install the recommended extensions in `.vscode/extensions.json`.

Install [poetry](https://python-poetry.org/docs/#installation).

Install required packages:

```shell
poetry install
```

## Development

Start the development server with automatic reload:

```shell
poetry shell
dev
```

or

```shell
poetry shell
uvicorn app.main:app --reload
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
uvicorn app.main:app
```
