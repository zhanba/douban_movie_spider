from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.dialects import postgresql
import settings

DeclarativeBase = declarative_base()

def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**settings.DATABASE))

def create_movies_table(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)

class Movies(DeclarativeBase):
    """Sqlalchemy movie model"""
    __tablename__ = "movies"


    title = Column('title', String)
    link = Column('link', String, nullable=True)
    location = Column('location', String, nullable=True)
    original_price = Column('original_price', String, nullable=True)
    price = Column('price', String, nullable=True)
    end_date = Column('end_date', DateTime, nullable=True)

    id = Column('id', postgresql.SERIAL)
    uuid = Column('uuid', postgresql.UUID)
    subject_id = Column('subject_id', STRING, length=1000)
    create_time = Column('create_time', TIMESTAMP)
    name = Column('name', STRING, length=1000) # movie name
    year = Column('year', INTEGER) # year
    cover_url = Column('cover_url', STRING, length=1000) # img cover url
    directors = Column('directors') # directors name and url
    writers = Column('writers') # writers name and url
    actors = Column('actors') # stars and url
    genres = Column('genres') # genres
    countries = Column('countries') # countries
    languages = Column('languages') # langaues
    release_date = Column('release_date') # premiere date and country
    running_time = Column('running_time') # running time
    alias = Column('alias') # alias
    imdb_link = Column('imdb_link') # imdb link
    rating = Column('rating') # the movie rating num
    rating_num = Column('rating_num') # the people num that rating movie
    summary = Column('summary') # summary
    tags = Column('tags') # the most used tags for the movie
