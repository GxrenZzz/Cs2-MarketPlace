# first endpoint 
from fastapi import FastAPI , Query , HTTPException , APIRouter
from app.modules.skins.data import skins
from app.modules.skins.schemas import SkinResponse
router = APIRouter()

@router.get("/skins",response_model=list[SkinResponse])   
def get_skins(
    weapon: str | None = None,
    limit: int = Query(default=10, gt=0),
    offset: int = Query(default=0, ge=0)
):
    filtered_skins = skins

    if weapon:
        filtered_skins = [
            skin for skin in filtered_skins
            if skin["weapon"] == weapon
        ]

    return filtered_skins[offset:offset + limit]



@router.get("/skins/{skin_id}",response_model=SkinResponse)
def get_uniue_skin(skin_id:int):
  skin = next((skin for skin in skins if skin["id"]== skin_id),None)
  if skin is None:
    raise HTTPException(status_code=404, detail="Skin Not Found")

  return skin