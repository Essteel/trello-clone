from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://trello_dev:password123@127.0.0.1:8080/trello'

db = SQLAlchemy(app)

@app.route('/')
def index():
    return "Hello, world!"


