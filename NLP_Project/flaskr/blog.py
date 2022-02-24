from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for,jsonify
)
from itsdangerous import json
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

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
        data = request.get_json()
        print(data)
        return jsonify(data)
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
