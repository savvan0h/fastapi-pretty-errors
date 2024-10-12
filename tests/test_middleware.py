from fastapi import FastAPI
from fastapi.testclient import TestClient

from fastapi_pretty_errors import PrettyErrorsMiddleware


def create_app() -> FastAPI:
    app = FastAPI()
    app.add_middleware(PrettyErrorsMiddleware)

    @app.get("/error")
    async def error_route():
        raise ValueError("This is a test error.")

    return app


# pytest needs '-s' flag to capture error
def test_error_route(capfd):
    app = create_app()
    client = TestClient(app)
    response = client.get("/error")
    assert response.status_code == 500
    assert response.json() == {"detail": "Unexpected error occured."}
    out, err = capfd.readouterr()
    assert "This is a test error." in err
