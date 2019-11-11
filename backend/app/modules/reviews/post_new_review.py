from flask import request

def _post_new_review():
    body = request.json
    return {"message": "OK"}
