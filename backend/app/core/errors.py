class AppException(Exception):
  def __init__(self,message : str ,code : int ,details : str | None = None ):
    self.message = message  
    self.code = code 
    self.details = details 
    super().__init__(message)


class SkinNotFoundError(AppException):
  def __init__(self):
    super().__init__(
      message="Skin Not Found",
      code=404,
      details="Skin not present in the exisiting Repository"
      )

class DuplicateSkinError(AppException):
  def __init__(self):
    super().__init__(
      message="Duplicate Skin",
      code=409,
      details="Skin Already Exist"
    )

