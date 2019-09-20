from flask import Flask 
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.sqla.form import InlineModelConverter

import models

from pages import home
from pages import edit

app = Flask(__name__)
models.db.init_app(app)
with app.app_context():
   models.db.create_all()


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/db.sql'
app.config['FLASK_ADMIN_SWATCH'] = 'simplex'
app.config['EXPLAIN_TEMPLATE_LOADING'] = True
app.secret_key = 'holaholaholahola'

admin = Admin(app, name='CMS DE JENERO', template_mode='bootstrap3')

admin.add_view(models.ModelView(models.AdminUser, models.db.session))
admin.add_view(models.PageModelView(models.Page, models.db.session))
admin.add_view(models.ModelView(models.Card, models.db.session))
admin.add_view(models.ModelView(models.Category, models.db.session))

app.register_blueprint(home.home)
app.register_blueprint(edit.edit)


app.run(host='0.0.0.0', debug=True)
