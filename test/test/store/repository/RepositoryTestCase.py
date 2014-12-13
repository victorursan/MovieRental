__author__ = 'victor'

import unittest
from store.repository.Repository import Repository
from store.domain.Entities.Client import Client
from store.domain.Validators.ClientValidator import ClientValidator


class RepositoryTestCase(unittest.TestCase):
  def setUp(self):
    self.__repo = Repository(ClientValidator())
    c1 = Client(1, "Steve", 12345678901)
    c2 = Client(2, "John", 12345678902)
    c3 = Client(3, "Ana", 12345678903)
    self.__repo.save(c1)
    self.__repo.save(c2)
    self.__repo.save(c3)

  def test_size(self):
    self.assertEqual(self.__repo.size(), 3)

  def test_get_all(self):
    l = self.__repo.get_all()
    self.assertEqual(len(l), 3)

  def test_save(self):
    c = Client(4, "Kate", 12345678904)
    self.__repo.save(c)
    self.assertEqual(self.__repo.size(), 4)

  def test_delete(self):
    self.__repo.delete(1)
    self.assertEqual(self.__repo.size(), 2)

  def test_find(self):
    c1 = Client(1, "Steve", 12345678901)
    c2 = self.__repo.find(1)
    self.assertEqual(c1, c2)

  def test_update(self):
    c = Client(1, "Kate", 12345678906)
    self.__repo.update(1, c)
    self.assertEqual(self.__repo.find(1), c)