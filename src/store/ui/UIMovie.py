__author__ = 'victor'

from store.domain.Validators.validators import StoreError, DuplicateIdError
from store.controller.MovieController import MovieController
from common.util import Util


class UIMovie(object):
  def __init__(self, movie_controller: MovieController):
    self.__movie_controller = movie_controller

  @staticmethod
  def description():
    return "Movie \n1 - Add \n2 - Remove \n3 - Update \n4 - List "

  def add(self):
    try:
      movie_id = int(input("id: "))
      title = str(input("Title: "))
      description = str(input("Description: "))
      genre = str(input("Genre: "))
      rating = float(input("Rating: "))
      self.__movie_controller.add_movie(movie_id, title, description, genre, rating)
    except ValueError as ve:
      print(ve)
    except StoreError as se:
      print(se)

  def remove(self):
    try:
      movie_id = int(input("id: "))
      self.__movie_controller.remove_movie(movie_id)
    except ValueError as ve:
      print(ve)
    except StoreError as se:
      print(se)

  def update(self):
    try:
      movie_id = int(input("id: "))
      title = str(input("Title: "))
      description = str(input("Description: "))
      genre = str(input("Genre: "))
      rating = float(input("Rating: "))
      self.__movie_controller.update_movie(movie_id, title, description, genre, rating)
    except ValueError as ve:
      print(ve)
    except StoreError as se:
      print(se)

  def list(self):
    Util.print_list(self.__movie_controller.list_movies())