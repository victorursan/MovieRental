__author__ = 'victor'

from store.domain.Entities.Movie import Movie
from store.repository.Repository import Repository


class MovieController(object):
  def __init__(self, repo: Repository):
    """ Initialize the repository

    :param repo: the repo
    """
    self.__repo = repo

  def list_movies(self):
    """ List all the movies in repo

    :return: a list of all movies
    """
    return self.__repo.get_all()

  def add_movie(self, movie_id, title, description, genre, rating):
    """ Add a movie with the specified parameters

    :param movie_id: the id of the movie
    :param title: the title of the movie
    :param description: the description of the movie
    :param genre: the genre of movie
    :param rating: the rating of the movie
    """
    movie = Movie(movie_id, title, description, genre, rating)
    self.__repo.save(movie)

  def remove_movie(self, movie_id):
    """ Removes a movie with the specific id

    :param movie_id: the id of the movie we want to remove
    """
    self.__repo.delete(movie_id)

  def find_movie(self, movie_id):
    """ Finds a movie with the specified id

    :param movie_id: the id of the movie we want to find

    :return: the movie with the specified id
    """
    return self.__repo.find(movie_id)

  def update_movie(self, movie_id, title, description, genre, rating):
    """ Updates a movie with the specified parameters

    :param movie_id: the id of the movie
    :param title: the new title of the movie
    :param description: the new description of the movie
    :param genre: de new genre of the movie
    :param rating: the new rating of the movie
    """
    movie = Movie(movie_id, title, description, genre, rating)
    self.__repo.update(movie_id, movie)