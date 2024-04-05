from flask import Flask
from flask_cors import CORS

import woz_data_opvragen

app = Flask(__name__)
CORS(app)

@app.route("/")
def helloWorld():
  return "Root Mount WOZ"

@app.route("/eigenaren/allen")
def eigenaren_allen():
  return woz_data_opvragen.toon_alle_eigenaren()


@app.route("/huizen/allen")
def huizen_allen():
  return woz_data_opvragen.toon_alle_huizen()