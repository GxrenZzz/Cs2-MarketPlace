# first endpoint 
from fastapi import FastAPI , Query , HTTPException , APIRouter ,status
from app.modules.skins.data import skins
from app.modules.skins.schemas import SkinResponse ,SkinCreate ,SkinRead
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

@router.post("/skins",response_model=SkinRead,status_code = status.HTTP_201_CREATED)
def create_skin(skin:SkinCreate):
    # converting incoming skin into a dict
    new_skin = skin.model_dump()

    # generating new_ids
    new_id = max(skin["id"] for skin in skins) + 1 

    # adding id into the dict 

    new_skin["id"] = new_id

    # appending the skin into the list 

    skins.append(new_skin)

    return new_skin 