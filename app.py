from flask import Flask, request
from flask_cors import CORS
import requests as req

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/register', methods=['POST'])
def register():
    username = request.args.get('username')

    return 'Hello, World!'

@app.route('/login', methods=['GET'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    if len(password) != 8:
        return {"exists":False}
    return req.login(username)