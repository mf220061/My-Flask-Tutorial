from flask import Flask, url_for, request, render_template, redirect, abort
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)
    print('This is never executed.')

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'
