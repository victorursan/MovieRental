__author__ = 'victor'


class Client(object):
  def __init__(self, Id, name, cnp):
    self.__Id = Id
    self.__name = name
    self.__cnp = cnp

  @property
  def Id(self):
    return self.__Id

  @property
  def name(self):
    return self.__name

  @property
  def cnp(self):
    return self.__cnp

  @Id.setter
  def Id(self, value):
    self.__Id = value

  @name.setter
  def name(self, value):
    self.__name = value

  @cnp.setter
  def cnp(self, value):
    self.__cnp = value

  def __str__(self):
    return "id: " + str(self.Id) + "\n" +\
           "Name: " + self.name + "\n" +\
           "CNP: " + str(self.cnp) + "\n"

  def __eq__(self, other):
    if type(self) is type(other):
      return self.__dict__ == other.__dict__
    return False

  def __ne__(self, other):
    return not self.__eq__(other)