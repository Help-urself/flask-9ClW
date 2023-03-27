from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    return """
    <style>
    b{
    background-color:dark;
    } 
    </style>
    <h1>Будущий сайт StarCard<h1>"""


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
