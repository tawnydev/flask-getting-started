from flask import Flask
from flask import url_for
from flask import request
from flask import render_template
from werkzeug.utils import secure_filename
from markupsafe import escape
from helper import valid_login, log_the_user_in
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('content_exemple.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    searchword = request.args.get('text', '')

    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', text=searchword, error=error)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)} profile'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['filename']
        path=os.getcwd()
        fileName= secure_filename(file.filename)
        print("path = ", path, "/", fileName)
        file.save(f"{path}/{fileName}")
        return render_template('hello.html', name=request.form['user'], upload=1)
    return render_template('hello.html', name=request.form['user'], upload=0)

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('show_user_profile', username='John Doe'))