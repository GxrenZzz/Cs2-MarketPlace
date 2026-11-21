from .repository import InMemorySkinRepository
from .service import SkinService

repository = InMemorySkinRepository()

def get_skin_service():
    return SkinService(repository)