from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import request
import os
import psycopg2

app = Flask(__name__)

DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')


# cur.execute(
#     "CREATE TABLE Persons (PersonID int,LastName varchar(255),FirstName varchar(255),Address varchar(255),City varchar(255));"
# )

# cur.execute(
#     "INSERT INTO Persons (personid, lastname, firstname, address, city) VALUES (1, 'anuttranon', 'sarin', '135 bangbon', 'bangkok');"
# )

# conn.commit()

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

@app.route('/getPersons')
def profile():
    cur = conn.cursor()
    cur.execute("SELECT * FROM Persons")
    records = cur.fetchall()
    return f'{records} persons'


with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
