from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def hello_geek():
    return '<h1>Hello from Flask & Docker</h2>'




if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port= 8000)
