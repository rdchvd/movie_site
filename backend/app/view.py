from app import app
from flask import request, jsonify, render_template
from models import Movie
import json

ml = ["james bond", "Jango free", "X-man"]

@app.route('/')
def index():
    return render_template('index.html')

#@app.errorhandler(404)
#def page_not_found(e):
#    return '404'

@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response
