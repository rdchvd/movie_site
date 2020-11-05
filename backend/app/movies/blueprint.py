from flask import Blueprint, render_template, request, redirect, url_for
from models import Movie, Genre
from .forms import MovieForm, UploadForm
from app import db
import json
from flask import jsonify
from sqlalchemy import func



movies = Blueprint('movies', __name__, template_folder='../../../frontend/templates')




def paginate(limit, offset):
    limit = int(request.args['limit'])
    offset = int(request.args['offset']) 

    movies = [movie.get_objects for movie in Movie.query.limit(limit).offset(offset).all()]
    
    items = db.session.query(func.count(Movie.id)).scalar()
    page_count = round(items/limit)
        
    return {
        'page_count': page_count,
        'movies': movies
        } 




def create():
    """Method gets needed form and renders html-file"""
    form = MovieForm()
    return render_template('movies/create_movie.html', form = form)




def create_movie():
    """Method filling the form and sending the data to database"""
    title = request.form['title']
    description = request.form['description']
    tagline = request.form['tagline']
    fees_in_world = request.form['fees_in_world']
    budget = request.form['budget']
    country = request.form['country']
    premiere = request.form['premiere']
    year = request.form['year']
    try:
        movie = Movie(
            title=title, description=description, tagline=tagline, fees_in_world=fees_in_world,
            budget=budget, country=country, premiere=premiere, year=year
            )
        db.session.add(movie)
        db.session.commit()
    except:
        print('Something wrong. Please, fill all fields and try again.')
    return redirect(url_for('movies.index'))




def edit(slug):
    movie = Movie.query.filter(Movie.slug==slug).first_or_404()
    form = MovieForm(obj=movie)
    return render_template('movies/edit_movie.html', movie=movie, form=form)


def edit_movie(slug):
    movie = Movie.query.filter(Movie.slug==slug).first_or_404()
    form = MovieForm(formdata=request.form, obj=movie)
    form.populate_obj(movie)


    db.session.commit()
    return redirect(url_for('movies.index'))
    




def index():
    q = request.args.get('q')
    limit = int(request.args['limit'])
    offset = int(request.args['offset']) 
    dictionary = paginate(limit, offset)
    movies = dictionary['movies']
    render_template('D:/frontend/templates/base.html', api_url="http://localhost:5000/movies/?limit=2&offset=0")
    

    if q:
        movies = Movie.query.filter(Movie.title.contains(q) | Movie.description.contains(q))
    else:
        movies = Movie.query

    return json.dumps({
        'current_page': 1,
        'has_next_page': True,
        'page_count': dictionary['page_count'],
        'movies': [movie.get_objects for movie in Movie.query.limit(limit).offset(offset).all()]
        })



def movie_detail(slug):
    movie = Movie.query.filter(Movie.slug == slug).first_or_404()
    genres = movie.genres
    return render_template('movies/movie_detail.html', movie = movie, genres = genres)


def genre_detail(slug):
    genre = Genre.query.filter(Genre.slug == slug).first_or_404()
    movies = genre.movies.all()
    return render_template('movies/genre_detail.html', genre = genre, movies = movies)



def upload(slug):
    form = UploadForm()
    movie = Movie.query.filter(Movie.slug == slug).first_or_404()

    if form.validate_on_submit():
        filename = secure_filename(form.file.data.filename)
        form.file.data.save(os.path.join(app.config['MEDIA_FOLDER'], filename))
        movie.image = os.path.join(app.config['MEDIA_FOLDER'], filename)
        db.session.commit()
        return redirect(url_for('movies.movie_detail', slug=slug))

    return render_template('movies/upload.html', form=form)




def delete_movie(slug):
    movie = Movie.query.filter(Movie.slug==slug).first_or_404()
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('movies.index'))


