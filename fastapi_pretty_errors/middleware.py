import sys

import pretty_errors
from fastapi import Request, Response, responses, status
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint


class PrettyErrorsMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, **pretty_errors_config):
        super().__init__(app)
        pretty_errors.configure(**pretty_errors_config)

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        try:
            response = await call_next(request)
            return response
        except Exception:
            pretty_errors.excepthook(*sys.exc_info())
            return responses.JSONResponse(
                content={"detail": "Unexpected error occured."},
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
