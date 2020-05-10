import os
from flask import Flask
from calculator import multiply


app = Flask(__name__)


@app.route("/<number>")
def calculate(number):
    response = multiply(int(number), 40)
    return str(response)


@app.route("/")
def info():
    return "please give a number in the URL"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
