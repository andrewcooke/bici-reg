from bici_reg.app import app
from bici_reg.db import db


def main():
    db.init_app(app)
    with app.app_context():
        db.create_all()


if __name__ == '__main__':
    main()
