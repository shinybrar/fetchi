"""Fixtures for testing."""

import pytest
from sanic_testing import TestManager

from fetchi.server import app


@pytest.fixture(autouse=True, scope="session")
def testapp():
    """Create a test app for testing."""
    return TestManager(app)
