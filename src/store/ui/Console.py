from store.controller.StatsController import StatsController
from store.ui.UIStats import UIStats

__author__ = 'victor'

from store.ui.UIMovie import UIMovie
from store.ui.UIClient import UIClient
from store.controller.ClientController import ClientController
from store.controller.MovieController import MovieController
from store.controller.RentReturnController import RentReturnController
from store.ui.UIRentReturn import UIRentReturn


class Console(object):
  def __init__(self, movie_controller: MovieController,
               client_controller: ClientController,
               rent_return_controller: RentReturnController,
               stats_controller: StatsController):
    self.__ui_movie = UIMovie(movie_controller)
    self.__ui_client = UIClient(client_controller)
    self.__ui_rent_return = UIRentReturn(rent_return_controller)
    self.__ui_stats = UIStats(stats_controller)

  def __second_menu(self, opt):
    movie = {"d": self.__ui_movie.description, 1: self.__ui_movie.add, 2: self.__ui_movie.remove,
             3: self.__ui_movie.update, 4: self.__ui_movie.list}
    client = {"d": self.__ui_client.description, 1: self.__ui_client.add, 2: self.__ui_client.remove,
              3: self.__ui_client.update, 4: self.__ui_client.list}
    menu = {1: movie, 2: client}
    active_menu = menu[opt]
    while True:
      try:
        print(active_menu["d"]() + "\nb - Back")
        opt = input("")
        if opt == "b":
          break
        opt = int(opt)
        active_menu[opt]()
      except ValueError:
        print("can't convert into int")
      except KeyError:
        print("The chosen option does not exist yet")

  def __third_menu(self, opt):
    option = {3: self.__ui_rent_return.rent_movie, 4: self.__ui_rent_return.return_movie,
              5: self.__ui_rent_return.list, 6: self.__ui_stats.sort_by_name, 7: self.__ui_stats.sort_by_borrow,
              8: self.__ui_stats.first_30_percent, 9: self.__ui_stats.extra_point}
    try:
      option[opt]()
    except ValueError:
      print("can't convert into int")
    except KeyError:
      print("The chosen option does not exist yet")

  def run_ui(self):
    while True:
      print("1 - Movie \n2 - Client \n3 - Rent \n4 - Return \n5 - Rented \n6 - Sort by name \n7 - Sort by borrow"
            "\n8 - First 30% \n9 - Extra \nx - Exit \n")
      opt = input("")
      if opt == "x":
        break
      try:
        opt = int(opt)
        if opt in [1, 2]:
          self.__second_menu(opt)
        else:
          self.__third_menu(opt)

      except ValueError:
        print("Can't convert into int")
      except KeyError:
        print("The chosen option does not exist yet")