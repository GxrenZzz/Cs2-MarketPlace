# first endpoint 

from fastapi import FastAPI , Query , HTTPException , APIRouter
from app.modules.skins.data import skins
router = APIRouter()

@router.get("/skins")
def get_skins(weapon : str | None = None,limit : int = Query(default=10,gt=0), offset : int = Query(default=0,ge=0)):
  # if user doesnt provide skin name -> give every skin 
  if weapon is None:
    filtered_skins = skins
  else:
    filtered_skins = [skin for skin in skins if skin["weapon"] == weapon]

  # PaginationLogic -> if user only needs limited skins 
  if limit == 0 or offset == -1:
    raise HTTPException(status_code=404,detail="Invalid pagination parameter")
  
  filtered_skins = filtered_skins[offset:limit+offset]
  

  return filtered_skins

@router.get("/skins/{skin_id}")
def get_uniue_skin(skin_id:int):
  skin = next((skin for skin in skins if skin["id"]== skin_id),None)
  if skin is None:
    raise HTTPException(status_code=404, detail="Skin Not Found")

  return skin