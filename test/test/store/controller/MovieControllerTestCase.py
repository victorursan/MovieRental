from store.domain.Validators.MovieValidator import MovieValidator

__author__ = 'victor'

import unittest
from store.repository.Repository import Repository
from store.controller.MovieController import MovieController
from store.domain.Entities.Movie import Movie


class MovieControllerTestCase(unittest.TestCase):
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
    self.__repo = Repository(MovieValidator())
    self.__repo.save(m1)
    self.__repo.save(m2)
    self.__repo.save(m3)
    self.__ctrl = MovieController(self.__repo)

  def test_list_movies(self):
    self.assertEqual(len(self.__ctrl.list_movies()), 3)

  def test_add_movie(self):
    self.__ctrl.add_movie(4, "Schindler's List",
                          "In Poland during World War II, Oskar Schindler gradually becomes concerned for his Jewish"
                          " workforce after witnessing their persecution by the Nazis.", "Biography", 8.9)
    self.assertEqual(len(self.__ctrl.list_movies()), 4)

  def test_remove_movie(self):
    self.__ctrl.remove_movie(1)
    self.assertEqual(len(self.__ctrl.list_movies()), 2)

  def test_find_movie(self):
    m1 = Movie(1, "The Shawshank Redemption",
               "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of"
               " common decency.", "Crime", 9.3)
    m2 = self.__ctrl.find_movie(1)
    self.assertEqual(m1, m2)

  def test_update_movie(self):
    m = Movie(1, "Schindler's List",
              "In Poland during World War II, Oskar Schindler gradually becomes concerned for his Jewish"
              " workforce after witnessing their persecution by the Nazis.", "Biography", 8.9)
    self.__ctrl.update_movie(1, m.title, m.description, m.genre, m.rating)
    self.assertEqual(m, self.__ctrl.find_movie(1))