from src import UserRepo
from flask import Flask, request
app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello_world():
    return "OLa, estou an aplicação"


@app.route("/", methods=["POST"])
def insert():
    userRepo = UserRepo()
    body = request.json

    userRepo.insert_user(body['name'])
    return "OK"
