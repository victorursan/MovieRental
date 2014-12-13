__author__ = 'victor'

import unittest
from test.store.repository.RepositoryTestCase import RepositoryTestCase


def suite():
  suites = unittest.TestSuite()
  suites.addTests(unittest.TestLoader().loadTestsFromTestCase(RepositoryTestCase))
  return suites