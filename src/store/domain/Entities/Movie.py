__author__ = 'victor'


class Movie(object):
  def __init__(self, Id, title, description, genre, rating):
    self.__Id = Id
    self.__title = title
    self.__description = description
    self.__genre = genre
    self.__rating = rating

  @property
  def Id(self):
    return self.__Id

  @property
  def title(self):
    return self.__title

  @property
  def description(self):
    return self.__description

  @property
  def genre(self):
    return self.__genre

  @property
  def rating(self):
    return self.__rating

  @Id.setter
  def Id(self, value):
    self.__Id = value

  @title.setter
  def title(self, value):
    self.__title = value

  @description.setter
  def description(self, value):
    self.__description = value

  @genre.setter
  def genre(self, value):
    self.__genre = value

  @rating.setter
  def rating(self, value):
    self.__rating = value

  def __str__(self):
    return "id: " + str(self.Id) + "\n" +\
           "Title: " + self.title + "\n" +\
           "Description: " + self.description + "\n" +\
           "Genre: " + self.genre + "\n" +\
           "Rating: " + str(self.rating) + "\n"

  def __eq__(self, other):
    if type(self) is type(other):
      return self.__dict__ == other.__dict__
    return False

  def __ne__(self, other):
    return not self.__eq__(other)