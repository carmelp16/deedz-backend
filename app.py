from flask import Flask, request
from flask_cors import CORS
from task_similarity import SemanticSim

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    semantic_sim = SemanticSim()
# # For comparing a single pair of strings
    a = semantic_sim.calc_cosine_sim("Cooking", "I need help with preparing soup")
# result: 0.38
    b = semantic_sim.calc_cosine_sim("Cooking", "I need help with walking the dog")

    return a + ', ' + b
# result: 0.06
