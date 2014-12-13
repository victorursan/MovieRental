__author__ = 'victor'

from store.domain.Validators.validators import DuplicateIdError, RepositoryError


class Repository(object):
  def __init__(self, validator):
    """Initializes the repository

    :param validator: the validator with which we validate the content
    """
    self.__items = {}
    self.__validator = validator

  def _add_item(self, item):
    """Saves a new item in the repository

    :param item: the new movie that is added to repo

    :raises DuplicateIdError: if the item already exists
    """
    if item.Id in self.__items.keys():
      raise DuplicateIdError("This item already exists")
    self.__validator.validate(item)
    self.__items[item.Id] = item

  def save(self, item):
    self._add_item(item)

  def delete(self, Id):
    """Deletes a item from the repo

    :param Id: the id of the item we want to remove

    :raises RepositoryError: if the item's id doesn't exist
    """
    if not Id in self.__items:
      raise RepositoryError("an item with the given id does not exist")
    self.__items.pop(Id)

  def update(self, Id, item):
    """Updates a movie's information

    :param Id: the id of the item we want to update
    :param item: the new item

    :raises RepositoryError: if the item's id doesn't exist
    """
    if not Id in self.__items:
      raise RepositoryError("an item with the given id does not exist")
    self.__items[Id] = item

  def find(self, Id):
    """Returns the item with the given Id.

    :param Id: the id of the item we want to find

    :raises RepositoryError: if the item's id doesn't exist

    :returns: the item with the given Id.
    """
    if not Id in self.__items.keys():
      raise RepositoryError("an item with the given id does not exist")
    return self.__items[Id]

  def size(self):
    """Returns the size of the repo

    :returns: the size of the repo
    """
    return len(self.__items)

  def get_all(self):
    """Returns a the list of all items in the repo

    :returns: a list with all items
    """
    return list(self.__items.values())