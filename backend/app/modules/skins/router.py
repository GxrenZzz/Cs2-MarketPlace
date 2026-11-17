# first endpoint 
from fastapi import APIRouter ,status , Depends 

from .schemas import SkinCreate , SkinRead ,SkinUpdate 
from .service import SkinService 
from .dependencies import get_skin_service

router = APIRouter() 


@router.get("/skins" ,response_model=list[SkinRead])
def get_all_skins(
    service : SkinService = Depends(get_skin_service)
    ):
    return service.get_all_skins() 

@router.get("/skins/{skin_id}",response_model=SkinRead)
def get_skin(
    skin_id:int,
    service : SkinService = Depends(get_skin_service)
):
    return service.get_skin(skin_id)

@router.post("/skins",response_model=SkinRead,status_code=status.HTTP_201_CREATED)
def create_skin(
    skin: SkinCreate,
    service : SkinService = Depends(get_skin_service)
):
    return service.create_skin(skin)

@router.put("/skins/{skin_id}",response_model=SkinRead)
def update_skin(
    skin_id:int,
    skin:SkinUpdate,
    service : SkinService = Depends(get_skin_service)
):
    return service.update_skin(skin_id,skin)

@router.delete("/skins/{skin_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_skin(
    skin_id:int,
    service : SkinService = Depends(get_skin_service)
):
    service.delete_skin(skin_id)
    return None

