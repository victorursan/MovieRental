__author__ = 'victor'

import unittest
from store.domain.Entities.Client import Client
from store.domain.Validators.ClientValidator import ClientValidator
from store.domain.Validators.validators import ValidatorError


class ClientValidatorTestCase(unittest.TestCase):
  def test_validate(self):
    c = Client(123, "Mike", 12345678910)
    try:
      ClientValidator().validate(c)
      self.assertTrue(True)
    except ValidatorError:
      self.assertFalse(True)

    c = Client(123, "", 123)
    try:
      ClientValidator().validate(c)
      self.assertTrue(False)
    except ValidatorError:
      self.assertFalse(False)