from os import environ

from flask import Flask

bcpasswd = environ['BCPASSWD']
secret_key = environ['SECRET_KEY']
password_salt = environ['PASSWORD_SALT']

app = Flask(__name__)

# https://flask-security-too.readthedocs.io/en/stable/quickstart.html#basic-sqlalchemy-application
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = secret_key
app.config['SECURITY_PASSWORD_SALT'] = password_salt
app.config['REMEMBER_COOKIE_SAMESITE'] = 'strict'
app.config['SESSION_COOKIE_SAMESITE'] = 'strict'
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://bici:{bcpasswd}@localhost/bici'
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_pre_ping': True,
}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'localhost'
app.config['SECURITY_REGISTERABLE'] = True
app.config['SECURITY_EMAIL_SENDER'] = 'andrew@acooke.org'  # CHANGE!!!
app.config['SECURITY_CONFIRMABLE'] = True
