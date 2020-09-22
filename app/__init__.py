from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from config import Config
from flask_login import  LoginManager, current_user, login_user, UserMixin, logout_user, login_required

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
login = LoginManager(app)



from app import main, models


if __name__ == "__main__":
   app.run()
