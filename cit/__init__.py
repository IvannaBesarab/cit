# Import flask and template operators
from flask import Flask, render_template, request, g

# Import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy

#Flask-Admin Initialization
from flask.ext.admin import Admin, BaseView, expose

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html',site_title=app.config["SITE_TITLE"])


class AdminPageView(BaseView):
    @expose('/')
    def index(self): 
        return self.render('index2.html') 
# created index2.html alongwith index.html in folder template

admin = Admin(app)
admin.add_view(AdminPageView(name='Hello'))
admin.add_view(AdminPageView(name='Hello 1', endpoint='test1', category='Test'))
admin.add_view(AdminPageView(name='Hello 2', endpoint='test2', category='Test'))
admin.add_view(AdminPageView(name='Hello 3', endpoint='test3', category='Test'))




