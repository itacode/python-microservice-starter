from dataclasses import dataclass
from typing import Optional


@dataclass
class ApplicationError(Exception):
    """
    Status code 500
    """

    code: Optional[str] = None
    detail: Optional[str] = None


class ResourceConflictError(ApplicationError):
    """
    Status code 409
    """


class ResourceNotFoundError(ApplicationError):
    """
    Status code 404
    """


class ParameterError(ApplicationError):
    """
    Status code 400
    """
