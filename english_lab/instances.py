from flask_bootstrap import Bootstrap5
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


database = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()
bootstrap5 = Bootstrap5()
