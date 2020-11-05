from app import db
from datetime import datetime
import re
from flask import jsonify

# from flask_security import UserMixin, RoleMixin

def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s)


movie_genres = db.Table('movie_genres',
                        db.Column('movie_id', db.Integer, db.ForeignKey('movie.id')),
                        db.Column('genre_id', db.Integer, db.ForeignKey('genre.id'))
)

movie_actors = db.Table('movie_actors',
                        db.Column('movie_id', db.Integer, db.ForeignKey('movie.id')),
                        db.Column('actor_id', db.Integer, db.ForeignKey('actor.id'))
)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique = True)
    tagline = db.Column(db.String(140))
    description = db.Column(db.Text)
    image = db.Column(db.String(150))
    year = db.Column(db.Integer)
    country = db.Column(db.String(70))
    premiere = db.Column(db.DateTime)
    budget = db.Column(db.Integer)
    fees_in_world = db.Column(db.Integer)
    reviews = db.relationship('Reviews', backref = 'movie', lazy = 'dynamic')
    movie_shots = db.relationship('MovieShots', backref = 'movie', lazy = 'dynamic')
    genres = db.relationship('Genre', secondary = movie_genres, backref = db.backref('movies', lazy = 'dynamic'))
    actors = db.relationship('Actor', secondary = movie_actors, backref = db.backref('movies', lazy = 'dynamic'))
    rating = db.relationship('Rating', backref='movie', lazy='dynamic')



    def __init__(self, *args, **kwargs):
        super(Movie, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)
    
    def __repr__(self):
        return '<Movie id: {}, title: {}>'.format(self.id, self.title)
    
    
    @property
    def get_objects(self):
        data = {
            'title': self.title,
            'tagline': self.tagline,
            'description': self.description,
            'year': self.year,
            'coutry': self.country,
        }
        return data
    



    #def json(self):
    #    data = {
    #        self.title,
    #        self.tagline,
    #        self.description,
    #        self.year,
    #        self.country,
    #        self.premiere
    #    }
    #    return jsonify(data)

class Genre(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(140))
    description = db.Column(db.Text)
    slug = db.Column(db.String(140), unique = True)

    def __init__(self, *args, **kwargs):
        super(Genre, self).__init__(*args, **kwargs)
        self.slug = slugify(self.title)
    
    def __repr__(self):
        return '<Genre id: {}, title: {}'.format(self.id, self.title)


class Actor(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    slug = db.Column(db.String(100), unique = True)
    age = db.Column(db.Integer)
    description = db.Column(db.Text)
    image = db.Column(db.LargeBinary)

    def __init__(self, *args, **kwargs):
        super(Actor, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)
    
    def __repr__(self):
        return '<Actor id: {}, name: {}'.format(self.id, self.name)


class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(140))
    name = db.Column(db.String(140))
    text = db.Column(db.Text)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))

    def __init__(self, *args, **kwargs):
        super(Reviews, self).__init__(*args, **kwargs)
    
    def __repr__(self):
        return '<Review id: {}, name: {}'.format(self.id, self.name)
    

class MovieShots(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    image = db.Column(db.LargeBinary)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))

    def __init__(self, *args, **kwargs):
        super(MovieShots, self).__init__(*args, **kwargs)
    
    def __repr__(self):
        return '<MovieShot id: {}, title: {}'.format(self.id, self.title)
    

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.Integer)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    rating_stars_id = db.Column(db.Integer, db.ForeignKey('rating_stars.id'))

    def __init__(self, *args, **kwargs):
        super(Rating, self).__init__(*args, **kwargs)

    def __repr__(self):
        return f'rs id: {self.id} mv id: {self.rating_stars_id}'

    
class RatingStars(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer)
    rating = db.relationship('Rating', backref='ratingstars', lazy='dynamic')

    def __init__(self, *args, **kwargs):
        super(RatingStars, self).__init__(*args, **kwargs)

    def __repr__(self):
        return f'ratingst: {self.id} value: {self.value}'


### Flask security

# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer(), primary_key = True)
#     email = db.Column(db.String(100), unique = True)
#     password = db.Column(db.String(255))
#     active = db.Column(db.Boolean())
#     roles = db.relationship('Role', secondary = roles_users, backref = db.backref('users', lazy = 'dynamic'))

# class Role(db.Model, RoleMixin):
#     id = db.Column(db.Integer(), primary_key = True)
#     name = db.Column(db.String(100), unique = True)
#     description = db.Column(db.String(255))
    
