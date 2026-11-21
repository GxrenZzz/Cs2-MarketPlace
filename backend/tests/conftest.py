
import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.modules.skins.dependencies import get_skin_service
from app.modules.skins.repository import InMemorySkinRepository
from app.modules.skins.service import SkinService


@pytest.fixture
def client():
    # Create a fresh repository for each test
    repository = InMemorySkinRepository()
    service = SkinService(repository)
    

    # Override the production dependency
    def override_get_skin_service():
        return service

    app.dependency_overrides[get_skin_service] = (
        override_get_skin_service
    )

    try:
        with TestClient(app) as test_client:
            yield test_client
    finally:
        app.dependency_overrides.clear()
