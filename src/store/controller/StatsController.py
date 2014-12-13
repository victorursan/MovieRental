from store.domain.Entities.Extra import Extra
from store.repository.Repository import Repository

__author__ = 'victor'


class StatsController(object):
  def __init__(self, repo: Repository, client_repo: Repository, movie_repo: Repository):
    """ Initialize the repository

    :param repo: the repo
    """
    self.__repo = repo
    self.__client_repo = client_repo
    self.__movie_repo = movie_repo

  def sort_by_name(self):
    clients_id = [x.Id for x in self.__repo.get_all()]
    clients = [self.__client_repo.find(Id) for Id in clients_id]
    return sorted(clients, key=lambda x: x.name, reverse=False)

  def sort_by_borrow(self):
    clients_with_rent = sorted(self.__repo.get_all(), key=lambda x: len(x.movies), reverse=True)
    return [self.__client_repo.find(x.Id) for x in clients_with_rent]

  def first_30_percent(self):
    l = self.sort_by_borrow()
    li = [{x.name: len(self.__repo.find(x.Id).movies)} for x in l]
    first_30 = int(len(li) / 3)
    return li[0:first_30 + 1]


  '''
    3. Print the list of movies (name, genre, rented_count) sorted after genre alphabetically and
  descendingly after rented_count (how many times it was rented).
  '''
  def get_count(self, movie_id):
    k = 0
    all_rented = []
    for r in self.__repo.get_all():
      all_rented.extend(r.movies)
    for m in all_rented:
      if m == movie_id:
        k += 1
    return k

  def extra_point(self):
    movies = self.__movie_repo.get_all()
    l = []
    for m in movies:
      e = Extra(m.title, m.genre, self.get_count(m.Id))
      l.append(e)
    return l.sort()