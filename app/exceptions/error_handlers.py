import logging
from dataclasses import asdict, dataclass
from http import HTTPStatus
from typing import Callable, Optional, Type, Union

from connexion import FlaskApp

from app.exceptions.application_errors import (
    ApplicationError,
    ParameterError,
    ResourceConflictError,
    ResourceNotFoundError,
)

logger = logging.getLogger(__name__)


@dataclass()
class ResponseBase:
    detail: Optional[str] = None
    status: Optional[int] = None
    title: Optional[str] = None
    type: Optional[str] = None
    code: Optional[str] = None


def handle_application_error(e: ApplicationError):
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    logger.exception("application error.")
    response_base = ResponseBase(
        detail=repr(e),
        status=http_status,
        title=http_status.phrase,
        code=e.code,
    )
    return (
        asdict(response_base),
        http_status,
    )


def handle_resource_conflict_error(e: ResourceConflictError):
    http_status = HTTPStatus.CONFLICT
    logger.exception("resource conflict error.")
    response_base = ResponseBase(
        detail=repr(e),
        status=http_status,
        title=http_status.phrase,
        code=e.code,
    )
    return (
        asdict(response_base),
        http_status,
    )


def handle_parameter_error(e: ParameterError):
    http_status = HTTPStatus.BAD_REQUEST
    logger.exception("parameter error.")
    response_base = ResponseBase(
        detail=repr(e),
        status=http_status,
        title=http_status.phrase,
        code=e.code,
    )
    return (
        asdict(response_base),
        http_status,
    )


def handle_resource_not_found_error(e: ResourceNotFoundError):
    http_status = HTTPStatus.NOT_FOUND
    logger.exception("resource not found.")
    response_base = ResponseBase(
        detail=repr(e),
        status=http_status,
        title=http_status.phrase,
        code=e.code,
    )
    return (
        asdict(response_base),
        http_status,
    )


def handle_exception(e: Exception):
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    logger.exception("internal error.")
    response_base = ResponseBase(
        detail=repr(e),
        status=http_status,
        title=http_status.phrase,
    )
    return (
        asdict(response_base),
        http_status,
    )


exception_to_handler: dict[Union[Type[Exception], int], Callable] = {
    ApplicationError: handle_application_error,
    ResourceConflictError: handle_resource_conflict_error,
    ParameterError: handle_parameter_error,
    ResourceNotFoundError: handle_resource_not_found_error,
    Exception: handle_exception,
}


def register_error_handlers(app: FlaskApp):
    for exception, handler in exception_to_handler.items():
        app.add_error_handler(exception, handler)
