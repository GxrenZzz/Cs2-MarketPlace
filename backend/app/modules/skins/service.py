from .exceptions import SkinNotFoundError

class SkinService:
  def __init__(self,repository):
    self.repository = repository

  def get_all_skins(self):
    return self.repository.get_all()

  def create_skin(self,skin):
    return self.repository.create_skin(skin)

  def get_skin(self,skin_id):
    skin_by_id = self.repository.get_skin_by_id(skin_id)

    if skin_by_id is None:
      raise SkinNotFoundError() 
    
    return skin_by_id

  def update_skin(self,skin_id,skin):
    updated_skin = self.repository.update_skin(skin_id,skin)

    if updated_skin is None:
      raise SkinNotFoundError() 

    return updated_skin
  
  def delete_skin(self,skin_id):
    deleted_skin =  self.repository.delete_skin(skin_id)

    if deleted_skin is None:
      raise SkinNotFoundError() 

    return deleted_skin

