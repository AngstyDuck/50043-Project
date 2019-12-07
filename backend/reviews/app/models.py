from app import db

class Reviews(db.Model):
    __tablename__ = 'amazonReviews'
    index = db.Column('index', db.Integer, primary_key=False)
    id = db.Column('asin', db.String(64), primary_key=True)
    helpful = db.Column('helpful', db.String(255))
    overall = db.Column('overall', db.Integer, primary_key=False)
    reviewText = db.Column('reviewText', db.String(255))
    reviewTime = db.Column('reviewTime', db.String(255))
    reviewerID = db.Column('reviewerID', db.String(255))
    reviewerName = db.Column('reviewerName', db.String(255))
    summary = db.Column('summary', db.String(255))
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
