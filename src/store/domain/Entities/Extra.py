__author__ = 'victor'


class Extra(object):
  def __init__(self, name, genre, count):
    self.__name = name
    self.__genre = genre
    self.__count = count

  @property
  def name(self):
    return self.__name

  @property
  def genre(self):
    return self.__genre

  @property
  def count(self):
    return self.__count

  @name.setter
  def name(self, value):
    self.__name = value

  @genre.setter
  def genre(self, value):
    self.__genre = value

  @count.setter
  def count(self, value):
    self.__count = value

  def __lt__(self, other):
    if self.genre < other.genre:
      return True
    return self.count > other.count

  def __gt__(self, other):
    return not self.__lt__(other)
