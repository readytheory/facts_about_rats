from flask import Flask

app = Flask(__name__)

from config import Config
from app import routes

c = Config()

app.config["SECRET_KEY"]=c.secret_key



