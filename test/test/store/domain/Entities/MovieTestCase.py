__author__ = 'victor'

import unittest
from store.domain.Entities.Movie import Movie


class MovieTestCase(unittest.TestCase):
  def test_create(self):
    m = Movie(1, "The Shawshank Redemption",
              "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of"
              " common decency.", "Crime", 9.3)

