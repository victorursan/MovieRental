from common.util import Util
from store.controller.RentReturnController import RentReturnController
from store.domain.Validators.validators import StoreError

__author__ = 'victor'


class UIRentReturn(object):
  def __init__(self, rent_return_controller: RentReturnController):
    self.__rent_return_controller = rent_return_controller

  def rent_movie(self):
    try:
      client_id = int(input("client_id: "))
      movie_id = int(input("movie_id: "))
      self.__rent_return_controller.rent_movie_to_client(client_id, movie_id)
    except ValueError as ve:
      print(ve)
    except StoreError as se:
      print(se)

  def return_movie(self):
    try:
      client_id = int(input("client_id: "))
      movie_id = int(input("movie_id: "))
      self.__rent_return_controller.return_movie_from_client(client_id, movie_id)
    except ValueError as ve:
      print(ve)
    except StoreError as se:
      print(se)

  def list(self):
    Util.print_list(self.__rent_return_controller.rented_movies())