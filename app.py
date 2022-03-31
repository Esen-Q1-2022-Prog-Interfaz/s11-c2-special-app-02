from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.auth import auth
from routes.todolist import todolist
from routes.orders import orders
from routes.orderdetails import orderDetails
from routes.store.store import store
from utils.db import db

app = Flask(__name__)

app.config.from_object("config.BaseConfig")

SQLAlchemy(app)

app.register_blueprint(auth)
