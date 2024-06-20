from flask import Flask, request
from flask_cors import CORS
import api_functions as req

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    phone = request.form.get('phone_number')
    street = request.form.get('street')
    number = request.form.get('number')
    city = request.form.get('city')
    suggestion = request.form.get('suggestion')
    photo = request.form.get('photo')
    return req.register(username, phone, street, number, city, suggestion, photo)

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

@app.route('/get_matches', methods=['POST'])
def match():
    return req.get_matches_lie()

@app.route('/get_user_by_id', methods=['GET'])
def get_by_id():
    return req.get_user_by_id(request.args.get('userId'))

@app.route('/upload_suggestion', methods=['POST'])
def upload_suggestion():
    return req.upload_help_suggestion(request.form.get('userId'), 
                                      request.form.get('suggestion'))

@app.route('/get_tasks', methods=['GET'])
def get_tasks():
    return req.get_matches(user_id=request.form.get('userId'))