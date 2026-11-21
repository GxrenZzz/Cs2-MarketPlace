from .schemas import SkinCreate, SkinUpdate


class InMemorySkinRepository:

  def __init__(self):
    self.skins = []

  def get_all(self):
    return self.skins.copy() # protecting repository List Structure 


  def create_skin(self,skin : SkinCreate):
    skin_data = skin.model_dump() 

    new_id = max((item["id"] for item in self.skins),default=0) + 1

    skin_data["id"] = new_id

    self.skins.append(skin_data)

    return skin_data

  def get_skin_by_id(self,skin_id):

    return next ((
          skin for skin in self.skins if skin["id"] == skin_id
    ),None )

  def update_skin(self,skin_id,skin:SkinUpdate):
    # check whether that skin exist 
    exisiting_skin = next((
      skin for skin in self.skins if skin["id"] == skin_id
    ),
    None 
    )
    if exisiting_skin is None:
       return None

    updated_data = skin.model_dump() 

    exisiting_skin.update(updated_data)

    return exisiting_skin


  def delete_skin(self,skin_id):
    skin =  next ((
      skin for skin in self.skins if skin["id"] == skin_id
    ),None )

    if skin is None:
      return None

    self.skins.remove(skin)

    return skin