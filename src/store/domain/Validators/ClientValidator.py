from store.domain.Entities.Client import Client

__author__ = 'victor'

from store.domain.Validators.validators import ValidatorError, Validator


class ClientValidator(Validator):
  @staticmethod
  def validate(client: Client):
    errors = []
    if not type(client.Id) is int:
      errors.append("id must be an int")
    if not client.name:
      errors.append("Name must be a non-empty string")
    if not type(client.cnp) is int:
      errors.append("CNP must be formed from digits")
    elif not client.cnp in range(10000000000, 100000000000):
        errors.append("CNP is not 11 digits long")
    if len(errors) > 0:
      raise ValidatorError(str(errors))