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
from flask import request
from datetime import datetime
from flask import current_app as app

def _helpful_review():
    print("ping - _helpful_review")
   # data = {
   # "reviewerID": "A3DE6XGZ2EPADS",
   # "asin": "B000F83SZQ",
   # "reviewerName": "WPY"
   # }
    data = request.json
    getQuery = "SELECT * FROM {0} WHERE asin=\'{1}\' and  reviewerID=\'{2}\' and reviewerName=\'{3}\' LIMIT 1 ".format(app.config["MYSQL_TABLE_REVIEWS"], data['asin'], data['reviewerID'],data['reviewerName'])
    connection = app.config["PYMYSQL_CONNECTION"]
    with connection.cursor() as cursor:
        cursor.execute(getQuery)
        query_result = cursor.fetchall()
        helpful_ = []
        helpful_.append(int(query_result[0]["helpful"][1])+1)
        helpful_.append(int(query_result[0]["helpful"][4])+1)
        cursor.execute("UPDATE {0} SET helpful = \'{1}\' WHERE id =\'{2}\'".format(app.config["MYSQL_TABLE_REVIEWS"],str(helpful_),query_result[0]["id"] ))
    connection.commit()
    cursor.exit()
    return{"Update": "Done"}

