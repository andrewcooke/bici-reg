from os import environ

from flask import Flask

app = Flask(__name__)
bcpasswd = environ['BCPASSWD']
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://bici:{bcpasswd}@localhost/bici'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
secret_key = environ['SECRET_KEY']
app.secret_key = secret_key
