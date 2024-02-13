# -*- coding: utf-8 -*
import os
from flask import request, Response
from app import application, db, admin
from app.models import User
from app.routes import *
from flask_admin.contrib.sqla import ModelView

# Database Table Auto-creation on Startup
with application.app_context():
    db.create_all()

# Admin Panel Basic Authentication Middleware
def check_auth(username, password):
    expected_username = os.environ.get("ADMIN_USERNAME", "admin")
    expected_password = os.environ.get("ADMIN_PASSWORD", "sokt2024")
    return username == expected_username and password == expected_password

def authenticate():
    return Response(
        "Could not verify your access level for this URL.\n"
        "You have to login with proper credentials", 401,
        {"WWW-Authenticate": 'Basic realm="Login Required"'}
    )

@application.before_request
def restrict_admin():
    if request.path.startswith("/admin/info"):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()

class UserView(ModelView):
    page_size = 100
    can_export = True
    column_display_pk = True
    column_searchable_list = ['name', 'email']
    column_filters = ['name', 'email']
    form_columns = ["id", "name", "course", "grade", "email", "reason"]

admin.add_view(UserView(User, db.session))

if __name__ == "__main__":
    application.run(host="0.0.0.0", debug=True)