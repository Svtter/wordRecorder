#!/usr/bin/env python3
# coding: utf-8

from flask import Flask, jsonify
from conf import directory
import json


app = Flask(__name__)

@app.route('/')
def show():
    with open(directory, 'r') as f:
        content = json.load(f)
        return jsonify(content), 200


if __name__ == '__main__':
    app.run()
