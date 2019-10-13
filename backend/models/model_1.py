from models.db import db
from sqlalchemy.dialects.mysql import TIMESTAMP, TINYINT
from werkzeug.security import check_password_hash
from datetime import datetime


class Model_1(db.Model):
    __tablename__ = 'table_1'
    user = db.Column(db.Integer, primary_key=True)
