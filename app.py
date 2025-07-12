from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(message="Hello, world!")

@app.route("/status")
def status():
    return jsonify(status="OK", service="CI App")

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return jsonify(result=a + b)

if __name__ == "__main__":
    app.run(debug=True)