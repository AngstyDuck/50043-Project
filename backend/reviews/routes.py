from flask import request, url_for, jsonify
from flask_api import FlaskAPI, status, exceptions

# local modules
from reviews import app
import sys
import os
dirname = os.path.dirname(__file__)
sys.path.insert(1, os.path.join(dirname, "api_logic"))
from review_list import _review_list
from post_new_review import _post_new_review




@app.route("/review_list/<asin_number>", methods=["GET"])
def review_list(asin_number):
    output = _review_list(asin_number)
    return jsonify(output), 200



@app.route("/post_new_review", methods=["POST"])
def post_new_review():
    body = request.get_json()
    output = _post_new_review(body)
    return jsonify(output), 200

@app.route("/test", methods=["GET"])
def test():
    return jsonify({"test message": "hello"})
