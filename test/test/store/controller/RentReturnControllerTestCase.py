from common.util import Util

__author__ = 'victor'

from store.controller.RentReturnController import RentReturnController
from store.domain.Entities.Client import Client
from store.domain.Entities.Movie import Movie
from store.domain.Entities.RentReturn import RentReturn
from store.domain.Validators.ClientValidator import ClientValidator
from store.domain.Validators.MovieValidator import MovieValidator
from store.domain.Validators.RentReturnValidator import RentReturnValidator
from store.repository.Repository import Repository
import unittest


class RentReturnControllerTestCase(unittest.TestCase):
  def setUp(self):
    m1 = Movie(1, "The Shawshank Redemption",
               "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of"
               " common decency.", "Crime", 9.3)
    m2 = Movie(2, "The Godfather",
               "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire"
               " to his reluctant son.", "Crime", 9.2)
    m3 = Movie(3, "Pulp Fiction",
               "The lives of two mob hit men, a boxer, a gangster's wife, and a pair of diner bandits intertwine "
               "in four tales of violence and redemption.", "Crime", 9.0)
    self.__movie_repo = Repository(MovieValidator())
    self.__movie_repo.save(m1)
    self.__movie_repo.save(m2)
    self.__movie_repo.save(m3)

    c1 = Client(1, "Steve", 12345678901)
    c2 = Client(2, "John", 12345678902)
    c3 = Client(3, "Ana", 12345678903)
    self.__client_repo = Repository(ClientValidator())
    self.__client_repo.save(c1)
    self.__client_repo.save(c2)
    self.__client_repo.save(c3)

    r1 = RentReturn(c1.Id, [m1.Id, m3.Id])
    self.__repo = Repository(RentReturnValidator())
    self.__repo.save(r1)
    self.__ctrl = RentReturnController(self.__repo, self.__client_repo, self.__movie_repo)

  def test_rented_movies_by_client(self):
    self.assertEqual(self.__ctrl.rented_movies_by_client(1), [1, 3])

  def test_rent_movie_to_client(self):
    self.__ctrl.rent_movie_to_client(1, 2)
    self.assertEqual(self.__ctrl.rented_movies_by_client(1), [1, 3, 2])

  def test_return_movie_from_client(self):
    self.__ctrl.return_movie_from_client(1, 1)
    self.assertEqual(self.__ctrl.rented_movies_by_client(1), [3])

  def test_rented_movies(self):
    self.assertEqual(len(self.__ctrl.rented_movies()), 1)
