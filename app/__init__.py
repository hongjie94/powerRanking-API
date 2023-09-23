from flask import Flask
from .extensions import api, mongo
from .routes import ns

def create_app():

  # Configure application
  app = Flask(__name__)

  app.config["MONGO_URI"] = "mongodb://localhost:27017/gpr"

  api.init_app(app)
  mongo.init_app(app)

  api.add_namespace(ns)

  return app