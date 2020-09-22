import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY='gvpTrsDaf5vgzIzdzC2XKA'
    SQLALCHEMY_DATABASE_URI='sqlite:///webshopDB.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS= False #kako bi se koristilo manje memorije
    SQLALCHEMY_ECHO= True
    ENV = 'development'


