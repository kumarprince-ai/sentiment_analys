from flask import Flask, request
from flask import jsonify

import src.sql_tools as tf

app = Flask(__name__)

@app.route("/")
def inicial():
    return "This is the Simpsons' quotes database"

@app.route("/quotes")
def rand_quotes():
    rand5 = tf.get5rand()
    return jsonify(rand5)

@app.route("/quotes/<name>")
def char(name):
    cuantas = request.args["how_many"]
    rand5_char = tf.char5(name,cuantas)
    return jsonify(rand5_char)

@app.route("/sentiment/<name>")
def sent(name):
    sent_char = tf.sent_analysis(name)
    return jsonify(sent_char)

app.run(debug=True)