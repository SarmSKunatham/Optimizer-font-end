from json import JSONDecoder, JSONEncoder
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for,jsonify
)
from itsdangerous import json
from werkzeug.exceptions import abort
import requests
import json
import ast

from flaskr.auth import login_required
from flaskr.db import get_db
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    db = get_db()
    # posts = db.execute(
    #     'SELECT p.id, title, body, created, author_id, username'
    #     ' FROM post p JOIN user u ON p.author_id = u.id'
    #     ' ORDER BY created DESC'
    # ).fetchall()
    return render_template('blog/index.html')

@bp.route('/product', methods=('GET', 'POST'))
def product():
    if request.method == "POST":
        text = request.form['text']
        headers = {
        'content-type': "application/json; charset=utf-8"
         }
        data = {"text": text}
        response = requests.request("POST", 'http://nlp1.optimizer.superai.me:10100/word_seg/count', data=json.dumps(data), headers=headers)
        # wordcloud = WordCloud(width = 1000, height = 500).generate_from_frequencies(response.json())
        # wordcloud.to_file('./flaskr/static/images/out.png')
        return response.json()
        
    return render_template('blog/product.html')

@bp.route('/service')
def service():

    return render_template('blog/service.html')
@bp.route('/sorry')
def sorry():
    return render_template('blog/sorry.html')

@bp.route('/about')
def about():
    return render_template('blog/about.html')
