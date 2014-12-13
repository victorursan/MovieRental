__author__ = 'victor'


class StoreError(Exception):
  def __init__(self, message=None, ex=None):
    Exception.__init__(self, message)
    self.__ex = ex
    self.__message = message
    
  @property
  def message(self):
    msg = self.__message if self.__message else ""
    if self.__ex is None:
      return msg
    msg = msg + " " + type(self.__ex).__name__ + ": " + str(self.__ex)
    return msg
     
  def __str__(self):
    return self.message


class ValidatorError(StoreError):
  pass


class RepositoryError(StoreError):
  pass


class DuplicateIdError(RepositoryError):
  pass


class Validator(object):
  @staticmethod
  def validate(item):
    pass