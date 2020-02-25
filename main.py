from flask import Flask, escape, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


@app.route("/mood")
def get_moods():
    happy = {
        "word": "happy",
        "pleasent": 5,
        "energy": 2.5
    }
    return jsonify([happy, "sad", "Angry", "idek"])
