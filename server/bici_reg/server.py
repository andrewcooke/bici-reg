from bici_reg.app import app
from bici_reg.db import db

db.init_app(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

