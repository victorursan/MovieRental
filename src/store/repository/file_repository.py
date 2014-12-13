from store.domain.Entities.Client import Client
from store.domain.Entities.Movie import Movie
from store.domain.Entities.RentReturn import RentReturn
from store.domain.Validators.validators import RepositoryError
from store.repository.Repository import Repository

__author__ = 'victor'


class ClientFileRepository(Repository):
  def __init__(self, validator, file_name):
    Repository.__init__(self, validator)
    self.__file_name = file_name
    self.__load_clients()

  def save(self, item):
    self._add_item(item)
    self.__save_client(item)

  def update(self, Id, item):
    super().update(Id, item)
    self.updatef()

  def delete(self, Id):
    super().delete(Id)
    self.updatef()

  def updatef(self):
    try:
      with open(self.__file_name, "w") as f:
        for client in self.get_all():
          s = str(client.Id) + " , " + client.name + " , " + str(client.cnp) + "\n"
          f.write(s)
    except Exception as ex:
      raise RepositoryError("Error opening file in updatef " + self.__file_name, ex)

  def __load_clients(self):
    try:
      with open(self.__file_name) as f:
        for line in f:
          try:
            arr = line.split(" , ")
            p = Client(int(arr[0]), arr[1], int(arr[2]))
            self._add_item(p)
          except Exception as ex:
            raise RepositoryError("Corrupted file", ex)
    except Exception as ex:
      raise RepositoryError("Error opening file " + self.__file_name, ex)

  def __save_client(self, client):
    try:
      with open(self.__file_name, "a") as f:
       s = str(client.Id) + " , " + client.name + " , " + str(client.cnp) + "\n"
       f.write(s)
    except Exception as ex:
      raise RepositoryError("Error opening file " + self.__file_name, ex)


class MovieFileRepository(Repository):
  def __init__(self, validator, file_name):
    Repository.__init__(self, validator)
    self.__file_name = file_name
    self.__load_movies()

  def save(self, item):
    self._add_item(item)
    self.__save_movie(item)

  def update(self, Id, item):
    super().update(Id, item)
    self.updatef()

  def delete(self, Id):
    super().delete(Id)
    self.updatef()

  def updatef(self):
    try:
      with open(self.__file_name, "w") as f:
        for movie in self.get_all():
          m = str(movie.Id) + " , " + movie.title + " , " + movie.description + " , " +\
           movie.genre + " , " + str(movie.rating) + "\n"
          f.write(m)
    except Exception as ex:
      raise RepositoryError("Error opening file in updatef " + self.__file_name, ex)

  def __load_movies(self):
    try:
      with open(self.__file_name) as f:
        for line in f:
          try:
            arr = line.split(" , ")
            m = Movie(int(arr[0]), arr[1], arr[2], arr[3], float(arr[4]))
            self._add_item(m)
          except Exception as ex:
            raise RepositoryError("Corrupted file", ex)
    except Exception as ex:
      raise RepositoryError("Error opening file " + self.__file_name, ex)

  def __save_movie(self, movie: Movie):
    try:
      with open(self.__file_name, "a") as f:
       m = str(movie.Id) + " , " + movie.title + " , " + movie.description + " , " +\
           movie.genre + " , " + str(movie.rating) + "\n"
       f.write(m)
    except Exception as ex:
      raise RepositoryError("Error opening file " + self.__file_name, ex)


class RentFileRepository(Repository):
  def __init__(self, validator, file_name):
    Repository.__init__(self, validator)
    self.__file_name = file_name
    self.__load_rents()

  def save(self, item):
    self._add_item(item)
    self.__save_rent(item)

  def update(self, Id, item):
    super().update(Id, item)
    self.updatef()

  def delete(self, Id):
    super().delete(Id)
    self.updatef()

  def updatef(self):
    try:
      with open(self.__file_name, "w") as f:
        for rent in self.get_all():
          r = str(rent.Id)
          for movie in rent.movies:
            r += " , " + str(movie)
          r += "\n"
          f.write(r)
    except Exception as ex:
      raise RepositoryError("Error opening file in updatef " + self.__file_name, ex)

  def __load_rents(self):
    try:
      with open(self.__file_name) as f:
        for line in f:
          try:
            arr = line.split(" , ")
            n = len(arr)
            l = []
            for element in arr[1 : n+1]:
              l.append(int(element))
            r = RentReturn(int(arr[0]), l)
            self._add_item(r)
          except Exception as ex:
            raise RepositoryError("Corrupted file", ex)
    except Exception as ex:
      raise RepositoryError("Error opening file " + self.__file_name, ex)

  def __save_rent(self, rent: RentReturn):
    try:
      with open(self.__file_name, "a") as f:
       r = str(rent.Id)
       for movie in rent.movies:
         r += " , " + movie
       r += "\n"
       f.write(r)
    except Exception as ex:
      raise RepositoryError("Error opening file " + self.__file_name, ex)