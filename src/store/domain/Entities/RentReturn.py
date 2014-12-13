__author__ = 'victor'


class RentReturn(object):
  def __init__(self, Id, movies):
    self.__Id = Id
    self.__movies = movies

  @property
  def Id(self):
    return self.__Id

  @property
  def movies(self):
    return self.__movies

  @Id.setter
  def Id(self, value):
    self.__Id = value

  @movies.setter
  def movies(self, value):
    self.__movies = value

  def __str__(self):
    return "Client: " + str(self.Id) + "\nMovies: " + str(self.movies) + "\n"

  def __eq__(self, other):
    if type(self) is type(other):
      return self.__dict__ == other.__dict__
    return False

  def __ne__(self, other):
    return not self.__eq__(other)