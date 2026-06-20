from flask import Flask,jsonify
import random
from datetime import datetime 
import platform

flk=Flask(__name__)
flk.json.sort_keys=False
@flk.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask API!",
                    "qoute":random.choice(quotes),
                    "status":"Running",
                    "time":datetime.now().isoformat(),
                    "Operating System":platform.system()})


quotes=[
    "Keep learning every day",
    "Success comes from consistency",
    "Practice makes perfect",
    "Learn from your mistakes",
    "Never stop improving"
]
@flk.route("/quotes")
def quotes_api():
    return jsonify({"quote": random.choice(quotes)})

@flk.route('/health')
def health():
    return jsonify({"status":"Running","message":"API is healthy","timestamp": datetime.now().isoformat()})

@flk.route('/student/<name>')
def student(name):
    return jsonify({"message" : f"Hello, {name}!"})

@flk.route('/random')
def random_quote():
    return jsonify({"number" : random.randint(1,1000)})

if __name__=="__main__":
    flk.run(debug=True,port=5001)