from flask import jsonify

def _post_new_review(body):
    output = {"message": "OK"}
    return jsonify(output)
