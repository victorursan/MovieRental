__author__ = 'victor'

import unittest
from test.store.domain.Entities.ClientTestCase import ClientTestCase
from test.store.domain.Entities.MovieTestCase import MovieTestCase
from test.store.domain.Entities.RentReturnTestCase import RentReturnTestCase


def suite():
  suites = unittest.TestSuite()
  suites.addTests(unittest.TestLoader().loadTestsFromTestCase(MovieTestCase))
  suites.addTests(unittest.TestLoader().loadTestsFromTestCase(ClientTestCase))
  suites.addTests(unittest.TestLoader().loadTestsFromTestCase(RentReturnTestCase))
  return suites
