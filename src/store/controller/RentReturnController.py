from store.domain.Entities.RentReturn import RentReturn

__author__ = 'victor'

from store.repository.Repository import Repository


class RentReturnController(object):
  def __init__(self, repo: Repository, client_repo: Repository, movie_repo: Repository):
    """ Initialize the repository

    :param repo: the repo
    """
    self.__repo = repo
    self.__client_repo = client_repo
    self.__movie_repo = movie_repo

  def rented_movies_by_client(self, client_id):
    self.check_content()
    return list(self.__repo.find(client_id).movies)

  def rented_movies(self):
    return [self.transform_rent_return(r) + "---------------" for r in self.__repo.get_all()]

  def transform_rent_return(self, rent_return):
    to_r = "" + str(self.__client_repo.find(rent_return.Id)) + "\n"
    for m in rent_return.movies:
      to_r += str(self.__movie_repo.find(m)) + "\n"
    return to_r

  def rent_movie_to_client(self, client_id, movie_id):
    self.check_content()
    if any(cl.Id == client_id for cl in self.__repo.get_all()):
      c = self.__repo.find(client_id)
      movies = list(c.movies)
      if not (movie_id in movies):
        movies.append(movie_id)
        self.__repo.update(client_id, RentReturn(client_id, movies))
    else:
      self.validate_client_movie(client_id, movie_id)
      movies = [movie_id]
      self.__repo.save(RentReturn(client_id, movies))

  def return_movie_from_client(self, client_id, movie_id):
    self.check_content()
    c = self.__repo.find(client_id)
    if c:
      movies = list(c.movies)
      if movie_id in movies:
        self.validate_client_movie(client_id, movie_id)
        movies = [m for m in movies if m != movie_id]
        self.__repo.update(client_id, RentReturn(client_id, movies))
        if len(movies) == 0:
          self.__repo.delete(client_id)

  def check_content(self):
    for cl in self.__repo.get_all():
      cl_movies = list(cl.movies)
      for movie in cl_movies:
        if not self.__movie_repo.find(movie):
          cl_movies = [m for m in cl_movies if m != movie]
          self.__repo.update(cl.Id, RentReturn(cl.Id, cl_movies))
      cl_id = cl.Id
      if not self.__client_repo.find(cl_id):
        self.__repo.delete(cl_id)

  def validate_client_movie(self, client, movie):
    if not (client in [c.Id for c in self.__client_repo.get_all()]):
      raise ValueError("no such client exists")
    if not (movie in [m.Id for m in self.__movie_repo.get_all()]):
      raise ValueError("no such movie exists")