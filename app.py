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
    username = request.form.get('username')
    number = request.form.get('phone_number')
    location = request.form.get('location')
    suggestion = request.form.get('suggestion')
    photo = request.form.get('photo')
    return req.register(username, number, location, suggestion, photo)

@app.route('/login', methods=['GET'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    if len(password) != 8:
        return {"exists":False}
    return req.login(username)

@app.route('/upload_task', methods=['POST'])
def upload():
    user_id = request.form.get('userId')
    task_text = request.form.get('task')
    time = request.form.get('hours_left')
    return req.upload_task(user_id, task_text, time_to_execute=time)