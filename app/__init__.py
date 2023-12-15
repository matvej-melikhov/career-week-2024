from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_admin import Admin
from app.config import Config


application = Flask(__name__)
application.config.from_object(Config)

db = SQLAlchemy(application)

migrate = Migrate(application, db)

mail = Mail(application)

admin = Admin(application, template_mode="bootstrap3", url="/admin/info")

