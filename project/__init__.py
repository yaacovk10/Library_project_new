from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
# # Serve static files
# app.static_folder = 'static'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.sqlite3'
app.config['SECRET_KEY'] = "random string"


db = SQLAlchemy(app)


from project.customers import customers
from project.loans import loans
from project.books import books
app.register_blueprint(customers)
app.register_blueprint(loans)
app.register_blueprint(books)


