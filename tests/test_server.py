"""Server tests."""

import pytest
from sanic import Sanic


@pytest.mark.asyncio
async def test_ping(testapp: Sanic):
    """Test the ping endpoint."""
    request, response = await testapp.asgi_client.get("/ping")
    assert request.method.lower() == "get"
    assert response.status == 200
    assert response.json == {"message": "pong"}


@pytest.mark.asyncio
async def test_fetch(testapp: Sanic):
    """Test the fetch endpoint."""
    request, response = await testapp.asgi_client.get("/v1/fetch/data.csv")
    assert request.method.lower() == "get"
    assert response.status == 200
    assert response.content_type == "text/csv"


@pytest.mark.asyncio
async def test_fetch_bad_filename(testapp: Sanic):
    """Test the fetch endpoint with a bad filename."""
    request, response = await testapp.asgi_client.get("/v1/fetch/not.there")
    assert request.method.lower() == "get"
    assert response.status == 404
