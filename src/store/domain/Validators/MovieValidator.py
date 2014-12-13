__author__ = 'victor'

from store.domain.Validators.validators import ValidatorError, Validator


class MovieValidator(Validator):
  @staticmethod
  def validate(movie):
    errors = []
    if not type(movie.Id) is int:
      errors.append("id must be an int")
    if not movie.title:
      errors.append("Title must be a non-empty string")
    if not movie.description:
      errors.append("Description must be a non-empty string")
    if not movie.genre:
      errors.append("Genre must be a non-empty string")
    if not type(movie.rating) is float:
      errors.append("The rating must be a number")
    elif not int(movie.rating) in range(0, 10):
        errors.append("The rating must be between 0...10")
    if len(errors) > 0:
      raise ValidatorError(str(errors))