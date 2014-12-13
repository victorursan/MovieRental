__author__ = 'victor'

from store.domain.Validators.validators import Validator, ValidatorError
from store.domain.Entities.RentReturn import RentReturn


class RentReturnValidator(Validator):
  @staticmethod
  def validate(rent_return: RentReturn):
    errors = []
    if not type(rent_return.Id) is int:
      errors.append("id must be an int")
    if any(type(x) != int for x in list(rent_return.movies)):
      errors.append("movies ids must me int")
    if len(list(rent_return.movies)) > len(set(list(rent_return.movies))):
      errors.append("duplicate id in movies")
    if len(errors) > 0:
      raise ValidatorError(str(errors))