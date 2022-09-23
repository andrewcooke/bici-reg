from flask import render_template_string
from flask_mailman import Mail
from flask_security import auth_required, hash_password, SQLAlchemyUserDatastore, Security

from bici_reg.app import app
from bici_reg.db import db, User, Role


mail = Mail(app)
db.init_app(app)
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
app.security = Security(app, user_datastore)


@app.route("/")
@auth_required()
def home():
    return render_template_string("Hello {{ current_user.email }}")


if __name__ == '__main__':
    with app.app_context():
        app.security.datastore.db.create_all()
        if not app.security.datastore.find_user(email="test@me.com"):
            app.security.datastore.create_user(email="test@me.com", password=hash_password("password"))
        app.security.datastore.db.session.commit()
    app.run()
