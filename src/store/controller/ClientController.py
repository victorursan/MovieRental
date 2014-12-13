__author__ = 'victor'

from store.domain.Entities.Client import Client
from store.repository.Repository import Repository


class ClientController(object):
  def __init__(self, repo: Repository):
    """ Initialize the repository

    :param repo: the repo
    """
    self.__repo = repo

  def list_clients(self):
    """ List all the clients in repo

    :return: a list of all clients
    """
    return self.__repo.get_all()

  def add_client(self, client_id, name, cnp):
    """ Add a client with the specified parameters

    :param client_id: the id of the client
    :param name: the name of the client
    :param cnp: the CNP of the client
    """
    client = Client(client_id, name, cnp)
    self.__repo.save(client)

  def remove_client(self, client_id):
    """ Remove a client with the specific id

    :param client_id: the id of the client we want to remove
    """
    self.__repo.delete(client_id)

  def find_client(self, client_id):
    """ Finds the client with the specified id

    :param client_id: the id of the client we want to find

    :return: the client with the specified id
    """
    return self.__repo.find(client_id)

  def update_client(self, client_id, name, cnp):
    """ Updates the client with the specified parameters

    :param client_id: the id of the client
    :param name: the new name of the client
    :param cnp: the new CNP of the client
    """
    client = Client(client_id, name, cnp)
    self.__repo.update(client_id, client)