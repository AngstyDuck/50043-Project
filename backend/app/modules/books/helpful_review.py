'''
### PUT /helpful_review
Example body from frontend
```json
{
 "reviewerID": "A3DE6XGZ2EPADS",
 "asin": "B000F83SZQ",
 "reviewerName": "WPY"
}
```
Feature:
To modify that particular reviewer's `"helpful"` array. Basically,
```c
helpful[0]++;
helpful[1]++;
```
Add 'one' to both sections of the array.
Only a return status of 200 is needed. The frontend will ignore any body elements.
'''

from flask import jsonify. request
from flask_jwt_extended import jwt_required, get_jwt_identity

reviews = app.config['']
metadata = app.config['']

def _helpful_review(data):

    data = json.loads(data)
    review = amazonreviews.query.filter_by(reviewerID=data['reviewerID'], asin=data['asin'], reviewerName=data['reviewerName']).first()
    helpful = review.helpful
    first = helpful[1]
    second = helpful[4]
    new_first = int(first) + 1
    new_second = int(second) + 1
    helpful_ = []
    helpful_.append(new_first)
    helpful_.append(new_second)
    helpful_ = str(helpful_)

    review.helpful = helpful_
    db.session.commit()

    return '200'
