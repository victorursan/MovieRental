__author__ = 'victor'

import unittest
from store.domain.Entities.RentReturn import RentReturn
from store.domain.Validators.validators import ValidatorError
from store.domain.Validators.RentReturnValidator import RentReturnValidator


class RentReturnValidatorTestCase(unittest.TestCase):
  def test_validate(self):
    r = RentReturn(123, [123, 124, 125])
    try:
      RentReturnValidator().validate(r)
      self.assertTrue(True)
    except ValidatorError:
      self.assertFalse(True)

    r = RentReturn(123, ["ana", 123, 123])
    try:
      RentReturnValidator().validate(r)
      self.assertTrue(False)
    except ValidatorError:
      self.assertFalse(False)