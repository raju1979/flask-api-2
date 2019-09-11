#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"
    
@app.route("/users")
def users():
    return jsonify(message="Hello how are you")

if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=True, port='1024')
