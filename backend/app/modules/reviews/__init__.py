from flask import request, url_for, jsonify, Blueprint
from flask_api import FlaskAPI, status, exceptions

# local modules
import sys
import os
dirname = os.path.dirname(__file__)
sys.path.insert(1, dirname)
from review_list import _review_list
from post_new_review import _post_new_review


module = Blueprint("reviews", __name__)


def _test():
    return jsonify({"test message": "hello"})

module.add_url_rule("/review_list", view_func=_review_list, methods=["GET"])
module.add_url_rule("/post_new_review", view_func=_post_new_review, methods=["POST"])
module.add_url_rule("/test", view_func=_test, methods=["GET"])

