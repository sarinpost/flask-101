from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        print('test', request.get_json())
        return f'post'
    else:
        return {
            "username": "asd",
            "theme": "theme",
        }


@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'


with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
