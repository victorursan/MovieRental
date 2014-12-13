__author__ = 'victor'

import unittest
from store.repository.Repository import Repository
from store.controller.ClientController import ClientController
from store.domain.Entities.Client import Client
from store.domain.Validators.ClientValidator import ClientValidator


class ClientControllerTestCase(unittest.TestCase):
  def setUp(self):
    c1 = Client(1, "Steve", 12345678901)
    c2 = Client(2, "John", 12345678902)
    c3 = Client(3, "Ana", 12345678903)
    self.__repo = Repository(ClientValidator())
    self.__repo.save(c1)
    self.__repo.save(c2)
    self.__repo.save(c3)
    self.__ctrl = ClientController(self.__repo)

  def test_list_client(self):
    self.assertEqual(len(self.__ctrl.list_clients()), 3)

  def test_add_client(self):
    self.__ctrl.add_client(4, "Kate", 12345678904)
    self.assertEqual(len(self.__ctrl.list_clients()), 4)

  def test_remove_client(self):
    self.__ctrl.remove_client(1)
    self.assertEqual(len(self.__ctrl.list_clients()), 2)

  def test_find_client(self):
    c1 = Client(1, "Steve", 12345678901)
    c2 = self.__ctrl.find_client(1)
    self.assertEqual(c1, c2)

  def test_update_client(self):
    c = Client(1, "Kate", 12345678906)
    self.__ctrl.update_client(1, c.name, c.cnp)
    self.assertEqual(c, self.__ctrl.find_client(1))