class AppException(Exception):
  def __init__(self,message,error_code,details=None):
    self.message = message
    self.error_code = error_code
    self.details = details
    super().__init__(message)


class SkinNotFoundError(AppException):
  def __init__(self):
    super().__init__(
      message="Skin Not Found",
      error_code=404,
      details="Skin not present in the exisiting Repository"
      )

class DuplicateSkinError(AppException):
  def __init__(self):
    super().__init__(
      message="Duplicate Skin",
      error_code=409,
      details="Skin Already Exist"
    )

