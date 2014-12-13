from store.domain.Validators.validators import StoreError

__author__ = 'victor'

from store.controller.ClientController import ClientController
from common.util import Util


class UIClient(object):
  def __init__(self, client_controller: ClientController):
    self.__client_controller = client_controller

  @staticmethod
  def description():
    return "Client \n1 - Add \n2 - Remove \n3 - Update \n4 - List"

  def add(self):
    try:
      client_id = int(input("id: "))
      name = str(input("name: "))
      cnp = int(input("CNP: "))
      self.__client_controller.add_client(client_id, name, cnp)
    except ValueError as ve:
      print(ve)
    except StoreError as se:
      print(se)

  def remove(self):
    try:
      client_id = int(input("id: "))
      self.__client_controller.remove_client(client_id)
    except ValueError as ve:
      print(ve)
    except StoreError as se:
      print(se)

  def update(self):
    try:
      client_id = int(input("id: "))
      name = str(input("name: "))
      cnp = int(input("CNP: "))
      self.__client_controller.update_client(client_id, name, cnp)
    except ValueError as ve:
      print(ve)
    except StoreError as se:
      print(se)

  def list(self):
    Util.print_list(self.__client_controller.list_clients())
