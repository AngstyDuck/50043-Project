from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions

# local modules
from reviews import app
import sys
sys.path.insert(1, "./reviews/api_logic")
from review_list import _review_list
from post_new_review import _post_new_review




@app.route("/review_list/<asin_number>", methods=["GET"])
def review_list(asin_number):
    try:
        output = _review_list(asin_number)
        return output, status.HTTP_200_OK
    except Exception as e:
        print(e)
        return {"error": e}, status.HTTP_INTERNAL_SERVER_ERROR



@app.route("/post_new_review", methods=["POST"])
def post_new_review():
    try:
        body = request.get_json()
        output = _post_new_review(body)
        return output, status.HTTP_200_OK
    except Exception as e:
        print(e)
        return {"error": e}, status.HTTP_INTERNAL_SERVER_ERROR

@app.route("/test", methods=["GET"])
def test():
    return "Hello"
