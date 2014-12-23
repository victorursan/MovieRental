from src.sorting_algorithms.Sorting import Sorting
from src.sorting_algorithms.algorithms.Algorithms import Algorithms
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
    Sorting.sort(clients, key=lambda x: x.name, reverse=False, algorithm=Algorithms.SHAKE_SORT)
    return clients

  def sort_by_borrow(self):
    clients_with_rent = self.__repo.get_all()
    Sorting.sort(clients_with_rent, key=lambda x: len(x.movies), reverse=True, algorithm=Algorithms.SELECTION_SORT)
    return [self.__client_repo.find(x.Id) for x in clients_with_rent]

  def first_30_percent(self):
    l = self.sort_by_borrow()
    li = [{x.name: len(self.__repo.find(x.Id).movies)} for x in l]
    first_30 = int(len(li) / 3)
    return li[0:first_30 + 1]

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