#!/usr/bin/env python
import os
from flask import Flask, abort, request, jsonify, g, url_for, render_template
import json
from random import randrange

# initialization
app = Flask(__name__)
grouchy_thoughts = json.load(open('grouch.json'))["quotes"]

@app.route('/grouchy')
def grouchy_saying():
    quote = grouchy_thoughts[randrange(len(grouchy_thoughts))]
    return render_template("quote.html", quote=quote, sayer="Oscar the grouch")

@app.route('/')
def hello():
    return "Spread the grouchiness!! Use /grouchy end point"

if __name__ == '__main__':
    if not os.path.exists('db.sqlite'):
        db.create_all()
    app.run(debug=True, port=7000)
    #app.run(ssl_context=('cert.pem', 'key.pem'))
    #app.run(debug=True, ssl_context='adhoc')
