from sanic import Sanic
from sanic_ext import openapi
from sanic.response import HTTPResponse, json
from sanic.request import Request
from sanic.log import logger

app = Sanic("fetchi")
app.config.HEALTH = True
app.static("/static/", "./fetchi/static/", strict_slashes=False, directory_view=True)  # type: ignore


@app.get("/ping")
@openapi.summary("Ping")
@openapi.description("Send a ping request to the server")
async def ping(request: Request) -> HTTPResponse:  # type: ignore
    """
    Send a ping request to the server

    Args:
        request (Request): Sanic request object

    Returns:
        HTTPResponse: Sanic HTTPResponse object
    """
    logger.info(f"ping request received from {request.ip}")
    return json({"message": "pong"})


@app.get(uri="/fetch/<filename:str>", version="v1")
@openapi.summary("Fetch")
@openapi.description("Fetch a file from the server")
async def fetch(request: Request, filename: str) -> HTTPResponse:  # type: ignore
    """
    Fetch a file from the server

    Args:
        request (Request): Sanic request object
        filename (str): Filename to fetch

    Returns:
        HTTPResponse: Sanic HTTPResponse object
    """
    logger.info(f"fetch request received from {request.ip} for {filename}")
    return json({"filename": filename})
