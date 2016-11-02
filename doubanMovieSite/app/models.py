from ext import db
from sqlalchemy.dialects import postgresql
from time import mktime

class Movie(db.Model):
    __tablename__ = 'movie'
    uuid = db.Column(postgresql.UUID, primary_key=True)
    update_time = db.Column(db.TIMESTAMP);
    subject_id = db.Column(db.String(50));
    name = db.Column(db.String(1000));
    year = db.Column(db.Integer);
    cover_url = db.Column(db.String(1000));
    directors = db.Column(postgresql.ARRAY(db.String(1000)));
    writers = db.Column(postgresql.ARRAY(db.String(1000)));
    actors = db.Column(postgresql.ARRAY(db.String(1000)));
    genres = db.Column(postgresql.ARRAY(db.String(1000)));
    countries = db.Column(postgresql.ARRAY(db.String(1000)));
    languages = db.Column(postgresql.ARRAY(db.String(200)));
    release_date = db.Column(db.String(1000));
    running_time = db.Column(db.Integer);
    alias = db.Column(postgresql.ARRAY(db.String(1000)));
    imdb_link = db.Column(db.String(1000));
    rating = db.Column(db.Float);
    rating_num = db.Column(db.Integer);
    summary = db.Column(db.TEXT);
    tags = db.Column(postgresql.ARRAY(db.String(1000)));

    def to_json(self):
        json_movie = {
            'uuid': self.uuid,
            'update_time': mktime(self.update_time.timetuple()),
            'subject_id': self.subject_id,
            'name': self.name,
            'year': self.year,
            'cover_url': self.cover_url,
            'directors': self.directors,
            'writers': self.writers,
            'actors': self.actors,
            'genres': self.genres,
            'countries': self.countries,
            'languages': self.languages,
            'release_date': self.release_date,
            'running_time': self.running_time,
            'alias': self.alias,
            'imdb_link': self.imdb_link,
            'rating': self.rating,
            'rating_num': self.rating_num,
            'summary': self.summary,
            'tags': self.tags
        }
        return json_movie

    def __repr__(self):
        return '<Movie %r>' % self.name
