from os import environ

from bici_reg.db import db


def main():
    bcpasswd = environ['BCPASSWD']
    db.create_engine(f'postgresql://bici:{bcpasswd}@localhost/bici', {})
    db.create_all()


if __name__ == '__main__':
    main()