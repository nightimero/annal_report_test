# -*- coding:utf-8 -*-
from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world'


@app.route('/user/<username>')
def show_user(username):
    return 'User is :%s' % username


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'

app.run(debug=True)
