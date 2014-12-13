__author__ = 'victor'

import unittest
from store.domain.Entities.RentReturn import RentReturn


class RentReturnTestCase(unittest.TestCase):
  def test_create(self):
    r = RentReturn(123, [123, 124, 125])
    self.assertEqual(r.Id, 123)
    self.assertEqual(r.movies, [123, 124, 125])
