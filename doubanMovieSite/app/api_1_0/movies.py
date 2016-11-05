from . import api
from ..models import Movie
from flask import jsonify
from sqlalchemy import create_engine, select, func
from sqlalchemy.sql import text
from ..config import database_url

engine = create_engine(database_url, echo=True)

@api.route('/movies/<string:uuid>')
def get_movie(uuid):
    movie = Movie.query.get_or_404(uuid)
    return jsonify(movie.to_json())

@api.route('/movies/')
def get_movies():
    movies = Movie.query.filter(text('year<1960'))\
        .filter(text('running_time>90'))\
        .filter(text('rating > 9')).all()
    return jsonify({
        'movies': [movie.to_json() for movie in movies],
        'count': len(movies)
    })

@api.route('/tags/')
def get_tags():
    s = text('SELECT count(tag) AS num, tag '
        'FROM ( '
        '        SELECT unnest(tags) AS tag '
        '        FROM movie ) AS T '
        'GROUP BY tag '
        'ORDER BY num DESC '
        'LIMIT 100 '
        'OFFSET 0')
    conn = engine.connect()
    res = conn.execute(s).fetchall()
    return jsonify({
        'tags': [r[1] for r in res],
        'nums': [r[0] for r in res]
    })

@api.route('/directors/')
def get_directors():
    pass
