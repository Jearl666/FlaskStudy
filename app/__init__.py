from flask import Flask
app = Flask(__name__, static_folder="static")
app.config.from_object("setting.DevelopmentConfig")
from app import routes

