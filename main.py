# -*- coding: utf-8 -*

from app import application
from app import migrate

from app.routes import *
from app.models import *

from app import admin
from flask_admin.contrib.sqla import ModelView

from app import db

class UserView(ModelView):
    page_size = 100
    can_export = True
    column_display_pk = True
    column_searchable_list = ['name', 'email']
    column_filters = ['name', 'email']
    form_columns = ["id", "name", "course", "grade", "email", "reason"]

admin.add_view(UserView(User, db.session))
admin.add_view(ModelView(Company, db.session))


if __name__ == "__main__":
    application.run(host="0.0.0.0", debug=True)