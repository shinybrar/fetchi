"""Fetchi Server Module."""

import stat
from pathlib import Path

from sanic import Sanic
from sanic.log import logger
from sanic.request import Request
from sanic.response import HTTPResponse, file, json
from sanic_ext import openapi

Sanic.start_method = "fork"

# Create the Sanic Web Application
app = Sanic("fetchi")

# Set the base directory from where the static files will be served
app.ctx.basedir = Path("./fetchi/static/")

# Enable the health check endpoint
app.config.HEALTH = True
app.config.HEALTH_ENDPOINT = True

# Enable the Directory view for the static files
app.static(
    "/static/", str(app.ctx.basedir), strict_slashes=True, directory_view=True
)  # type: ignore


@app.get("/ping")
@openapi.summary("Ping")
@openapi.description("Send a ping request to the server")
async def ping(request: Request) -> HTTPResponse:  # type: ignore
    """Send a ping request to the server.

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
    """Fetch a file from the server.

    Args:
        request (Request): Sanic request object
        filename (str): Filename to fetch

    Returns:
        HTTPResponse: Sanic HTTPResponse object
    """
    logger.info(f"fetch request received from {request.ip} for {filename}")

    try:
        filepath: Path = app.ctx.basedir / filename
        # Check if the filepath exists and is a file
        if not filepath.exists() and not filepath.is_file():
            return json({"error": "file not found"}, status=404)
        # Check if we can read the file
        if not (filepath.stat().st_mode & stat.S_IRUSR):
            return json({"error": "file not readable"}, status=403)
        # Serve the static file
        return await file(
            location=filepath,
            filename=filename,
        )
    except Exception as error:
        logger.error(f"unknown server error: {error}")
        return json({"error": f"{str(error)}"}, status=500)
