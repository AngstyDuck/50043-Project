from app import db

class Reviews(db.Model):
    __tablename__ = 'amazonReviews'
    index = db.Column('index', db.Integer, primary_key=False)
    id = db.Column('asin', db.Unicode, primary_key=True)
    helpful = db.Column('helpful', db.Unicode)
    overall = db.Column('overall', db.Integer, primary_key=False)
    reviewText = db.Column('reviewText', db.Unicode)
    reviewTime = db.Column('reviewTime', db.Unicode)
    reviewerID = db.Column('reviewerID', db.Unicode)
    reviewerName = db.Column('reviewerName', db.Unicode)
    summary = db.Column('summary', db.Unicode)
    unixReviewTime = db.Column('unixReviewTime', db.DateTime)

'''
| index          | bigint(20) | YES  | MUL | NULL    |       |
| asin           | text       | YES  |     | NULL    |       |
| helpful        | text       | YES  |     | NULL    |       |
| overall        | bigint(20) | YES  |     | NULL    |       |
| reviewText     | text       | YES  |     | NULL    |       |
| reviewTime     | text       | YES  |     | NULL    |       |
| reviewerID     | text       | YES  |     | NULL    |       |
| reviewerName   | text       | YES  |     | NULL    |       |
| summary        | text       | YES  |     | NULL    |       |
| unixReviewTime | bigint(20) | YES  |     | NULL    |       |

'''
