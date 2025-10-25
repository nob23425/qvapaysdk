from httpx import Response

from .errors import QvaPayError


def validate_response(response: Response):
    if response.status_code != 200:
        raise QvaPayError(response.status_code)
