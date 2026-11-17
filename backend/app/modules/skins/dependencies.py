from .service import SkinService  
from .repository import InMemorySkinRepository

repository = InMemorySkinRepository()

def get_skin_service():
    return SkinService(repository)