__author__ = 'victor'

import unittest
from test.store.domain.Validators.ClientValidatorTestCase import ClientValidatorTestCase
from test.store.domain.Validators.MovieValidatorTestCase import MovieValidatorTestCase
from test.store.domain.Validators.RentReturnValidatorTestCase import RentReturnValidatorTestCase


def suite():
  suites = unittest.TestSuite()
  suites.addTests(unittest.TestLoader().loadTestsFromTestCase(ClientValidatorTestCase))
  suites.addTests(unittest.TestLoader().loadTestsFromTestCase(MovieValidatorTestCase))
  suites.addTests(unittest.TestLoader().loadTestsFromTestCase(RentReturnValidatorTestCase))
  return suites