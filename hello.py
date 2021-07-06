from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    print("It is print _________")
    return "<h2>Hello, World! From Flask. New ;-) !!!</h2>"