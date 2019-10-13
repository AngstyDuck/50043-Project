from flask import request, jsonify

from models.db import db
from models.model_1 import Model_1

def endpoint_1():
    user = str(request.json.get("user"))
    message = {}
    user = db.session.query(Model_1).filter(
        Model_1.user == user
    ).first()
    return jsonify(message), 400
