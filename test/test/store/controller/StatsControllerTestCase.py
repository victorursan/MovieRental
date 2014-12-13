from store.controller.StatsController import StatsController
from store.domain.Entities.Client import Client
from store.domain.Entities.Movie import Movie
from store.domain.Entities.RentReturn import RentReturn
from store.domain.Validators.ClientValidator import ClientValidator
from store.domain.Validators.MovieValidator import MovieValidator
from store.domain.Validators.RentReturnValidator import RentReturnValidator
from store.repository.Repository import Repository

__author__ = 'victor'

import unittest


class StatsControllerTestCase(unittest.TestCase):
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
    r2 = RentReturn(c2.Id, [m2.Id, m3.Id])
    r3 = RentReturn(c3.Id, [m3.Id, m1.Id, m2.Id])
    self.__repo = Repository(RentReturnValidator())
    self.__repo.save(r1)
    self.__repo.save(r2)
    self.__repo.save(r3)

    self.__ctrl = StatsController(self.__repo, self.__client_repo, self.__movie_repo)

  def test_sort_by_name(self):
    self.assertEqual(self.__ctrl.sort_by_name()[0].Id, 3)

  def test_sort_by_borrow(self):
    self.assertEqual(self.__ctrl.sort_by_borrow()[0].Id, 3)

  def test_first_30_percent(self):
    self.assertEqual(self.__ctrl.first_30_percent()[0], {"Ana": 3})

  def test_extra_point(self):
    self.assertEqual(self.__ctrl.extra_point()[0], {'name': 'Pulp Fiction', 'genre': 'Crime', 'rented_count': 3})