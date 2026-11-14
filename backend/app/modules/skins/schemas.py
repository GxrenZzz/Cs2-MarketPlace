from pydantic import BaseModel , model_validator ,Field
from enum import Enum

class SkinResponse(BaseModel):
  id:int
  name:str
  weapon:str
  rarity:str
  price:float

class Rarity(str,Enum):
  CONSUMER = "Consumer"
  INDUSTRIAL = "Industrial"
  MIL_SPEC = "Mil-Spec"
  RESTRICTED = "Restricted"
  CLASSIFIED = "Classified"
  COVERT = "Covert"

class Wear(str,Enum):
  FACTORY_NEW = "Factory New"
  MINIMAL_WEAR = "Minimal Wear"
  FIELD_TESTED = "Field-Tested"
  WELL_WORN = "Well-Worn"
  BATTLE_SCARRED = "Battle-Scarred"

class SkinCreate(BaseModel):
  name:str
  weapon:str
  rarity:Rarity
  wear:Wear
  min_float:float = Field(ge=0,le=1)
  max_float:float = Field(ge=0,le=1)
  price:float = Field(ge=0)

  @model_validator(mode="after")
  def validate_float(self):
    if self.min_float > self.max_float:
      raise ValueError("Min Value cant exceed Max Value")
    return self 

class SkinRead(BaseModel):
  id:int
  name:str
  weapon:str
  rarity:Rarity
  wear:Wear
  min_float:float 
  max_float:float
  price:float


