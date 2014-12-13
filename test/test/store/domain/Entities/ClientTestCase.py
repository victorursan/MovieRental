__author__ = 'victor'

import unittest
from store.domain.Entities.Client import Client


class ClientTestCase(unittest.TestCase):
  def test_create(self):
    c = Client(1, "Steve", 1950101221144)
    self.assertEqual(c.Id, 1)
    self.assertEqual(c.name, "Steve")
    self.assertEqual(c.cnp, 1950101221144)
    self.assertEqual(c, Client(1, "Steve", 1950101221144))
