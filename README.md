# Python microservice starter
A boilerplate to start developing microservices.

## API example
Base path: [http://localhost:5001/api/v1/my_service](http://localhost:5001/api/v1/my_service)
- GET `​/files` - List uploaded ﬁles
- POST `​/files` - Upload a ﬁle
- DELETE `​/files​/{name}` - Delete a ﬁle

Interactive API documentation: [http://localhost:5001/api/v1/my_service/ui](http://localhost:5001/api/v1/my_service/ui)

## Features
- [Connexion](https://connexion.readthedocs.io/en/latest/index.html) a framework on top of Flask that automagically validates and handles HTTP requests defined using [OpenAPI](https://www.openapis.org/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/) development server with live reload
- [Waitress](https://docs.pylonsproject.org/projects/waitress/en/latest/) production server
- `app/api/openapi/api.oas.yml` API designed using [OpenAPI Specification](https://swagger.io/specification/)
- Interactive API documentation (Swagger UI)
- `.env` file for the app configuration
- `Doker` and `docker-compose.yml` to run the prodution server
- [openapi-generator-cli](https://github.com/OpenAPITools/openapi-generator-cli) configured to generate some clients
- [SQLAlchemy](https://www.sqlalchemy.org/)
- MySQL database with docker compose
- [sqlacodegen](https://github.com/agronholm/sqlacodegen) a tool that reads the structure of an existing database and generates the appropriate SQLAlchemy model code 

## Installation
It requires [pipenv](https://pipenv.pypa.io/en/latest/).

```shell
pipenv install --dev
```

## Development server
Start the development server with automatic reload.
```shell
pipenv shell
flask run
```

## Production server
```shell
waitress-serve --port=5001 --call app:create_app
```

## Docker
Start
```shell
docker-compose up -d --build
```
Stop
```shell
docker-compose down
```

## SQLAlchemy model code generation
You need the database available to execute the following command
```shell
pipenv run gen_sqlacode
```
