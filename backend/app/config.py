import os
class Configuration(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI ="postgresql+psycopg2://darina:orirul89@localhost/mroom"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', None)
    STATIC_FOLDER='D:\\mainProject\\frontend\\static'
    STATIC_PATH='D:\\mainProject\\frontend\\static'
    MEDIA_FOLDER ='D:\\mainProject\\frontend\\media' 
    API_URL = "http://localhost:5000/movies/?limit=2&offset=0"   
