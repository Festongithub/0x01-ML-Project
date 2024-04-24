#!/usr/bin/python3

from actor import Actor
from base import Session
from contact_details import ContactDetails
from movie import Movie

session = Session()

movies = session.query(Movie).all()

print('\n### All movies:')
for movie in movies:
    print(f'{movies.title} was released on {movie.release_date}')
    print('')
    
