from pydantic import BaseModel

class SkinResponse(BaseModel):
  id:int
  name:str
  weapon:str
  rarity:str
  price:float


class SkinCreate(BaseModel):
  name:str
  weapon:str
  rarity:str
  price:float


