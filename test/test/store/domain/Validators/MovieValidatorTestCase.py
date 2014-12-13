__author__ = 'victor'

import unittest
from store.domain.Entities.Movie import Movie
from store.domain.Validators.MovieValidator import MovieValidator
from store.domain.Validators.validators import ValidatorError


class MovieValidatorTestCase(unittest.TestCase):
  def test_validate(self):
    m = Movie(1, "The Shawshank Redemption",
              "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts"
              " of common decency.", "Crime", 9.3)
    try:
      MovieValidator().validate(m)
      self.assertTrue(True)
    except ValidatorError:
      self.assertFalse(True)

    m = Movie(1, "",
              "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts"
              " of common decency.", "", 12)
    try:
      MovieValidator().validate(m)
      self.assertTrue(False)
    except ValidatorError:
      self.assertFalse(False)
