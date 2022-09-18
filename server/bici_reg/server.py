from bici_reg.app import app
from bici_reg.db import db
from bici_reg.login import login_manager

db.init_app(app)
login_manager.init_app(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

