import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123456@localhost:5432/douban'

database_url = 'postgresql+psycopg2://postgres:123456@localhost:5432/douban'
