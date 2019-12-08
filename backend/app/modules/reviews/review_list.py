import sys
import json
import copy
from datetime import datetime
from flask import Flask
from flask import current_app as app

sample_output = {"review":[
                    {
                        "reviewerID": "A1F6404F1VG29J",
                        "asin": "B000F83SZQ",
                        "reviewerName": "Avidreader",
                        "helpful": [0, 0],
                        "reviewText":
                        "I enjoy vintage books and movies so I enjoyed reading this book.  The plot was unusual.  Don't think killing someone in self-defense but leaving the scene and the body without notifying the police or hitting someone in the jaw to knock them out would wash today.Still it was a good read for me.",
                        "overall": 5.0,
                        "summary": "Nice vintage story",
                        "reviewTime": "June 8, 2019"
                    },
                    {
                      "reviewerID": "AN0N05A9LIJEQ",
                      "asin": "B000F83SZQ",
                      "reviewerName": "critters",
                      "helpful": [
                        2,
                        2
                      ],
                      "reviewText": "This book is a reissue of an old one; the author was born in 1910. It's of the era of, say, Nero Wolfe. The introduction was quite interesting, explaining who the author was and why he's been forgotten; I'd never heard of him.The language is a little dated at times, like calling a gun a &#34;heater.&#34;  I also made good use of my Fire's dictionary to look up words like &#34;deshabille&#34; and &#34;Canarsie.&#34; Still, it was well worth a look-see.",
                      "overall": 4,
                      "summary": "Different...",
                      "reviewTime": "May 18, 2019"
                    },
                    {
                      "reviewerID": "A795DMNCJILA6",
                      "asin": "B000F83SZQ",
                      "reviewerName": "dot",
                      "helpful": [
                        2,
                        2
                      ],
                      "reviewText": "This was a fairly interesting read.  It had old- style terminology.I was glad to get  to read a story that doesn't have coarse, crasslanguage.  I read for fun and relaxation......I like the free ebooksbecause I can check out a writer and decide if they are intriguing,innovative, and have enough of the command of Englishthat they can convey the story without crude language.",
                      "overall": 4,
                      "summary": "Oldie",
                      "reviewTime": "September 20, 2014"
                    },
                    {
                      "reviewerID": "A1FV0SX13TWVXQ",
                      "asin": "B000F83SZQ",
                      "reviewerName": "Elaine H. Turley Montana Songbird",
                      "helpful": [
                        1,
                        1
                      ],
                      "reviewText": "I'd never read any of the Amy Brewster mysteries until this one..  So I am really hooked on them now.",
                      "overall": 5,
                      "summary": "I really liked it.",
                      "reviewTime": "June 8, 2019"
                    },
                    {
                      "reviewerID": "A3SPTOKDG7WBLN",
                      "asin": "B000F83SZQ",
                      "reviewerName": "Father Dowling Fan",
                      "helpful": [
                        0,
                        1
                      ],
                      "reviewText": "If you like period pieces - clothing, lingo, you will enjoy this mystery.  Author had me guessing at least 2/3 of the way through.",
                      "overall": 4,
                      "summary": "Period Mystery",
                      "reviewTime": "June 8, 2019"
                    },
                    {
                      "reviewerID": "A1RK2OCZDSGC6R",
                      "asin": "B000F83SZQ",
                      "reviewerName": "ubavka seirovska",
                      "helpful": [
                        0,
                        0
                      ],
                      "reviewText": "A beautiful in-depth character description makes it like a fast pacing movie. It is a pity Mr Merwin did not write 30 instead only 3 of the Amy Brewster mysteries.",
                      "overall": 4,
                      "summary": "Review",
                      "reviewTime": "June 8, 2019"
                    },
                    {
                      "reviewerID": "A2HSAKHC3IBRE6",
                      "asin": "B000F83SZQ",
                      "reviewerName": "Wolfmist",
                      "helpful": [
                        0,
                        0
                      ],
                      "reviewText": "I enjoyed this one tho I'm not sure why it's called An Amy Brewster Mystery as she's not in it very much. It was clean, well written and the characters well drawn.",
                      "overall": 4,
                      "summary": "Nice old fashioned story",
                      "reviewTime": "June 8, 2019"
                    },
                    {
                      "reviewerID": "A3DE6XGZ2EPADS",
                      "asin": "B000F83SZQ",
                      "reviewerName": "WPY",
                      "helpful": [
                        1,
                        1
                      ],
                      "reviewText": "Never heard of Amy Brewster. But I don't need to like Amy Brewster to like this book. Actually, Amy Brewster is a side kick in this story, who added mystery to the story not the one resolved it. The story brings back the old times, simple life, simple people and straight relationships.",
                      "overall": 4,
                      "summary": "Enjoyable reading and reminding the old times",
                      "reviewTime": "June 8, 2019"
                    }
                ]}

def _review_list(asin_number):
    query = "SELECT * FROM {0} WHERE asin=\'{1}\'".format(app.config["MYSQL_TABLE_REVIEWS"], str(asin_number))
    connection = app.config["PYMYSQL_CONNECTION"].cursor()
    with connection as cursor:
        cursor.execute(query)
        query_result = cursor.fetchall()
        query_result_edited = copy.deepcopy(query_result)

        for i in query_result_edited:
            # change datatype of column 'helpful' from string to list
            # e.g. from "[0, 0]" to [0, 0] of datatype 'list'
            helpful_val = i["helpful"]
            helpful_val = helpful_val.split(", ")
            helpful_val[0] = int(helpful_val[0][1:])
            helpful_val[1] = int(helpful_val[1][:-1])
            i["helpful"] = helpful_val

            # change value reviewTime to match format "month date, year"
            reviewTime_val = int(i["unixReviewTime"])
            reviewTime_val = datetime.fromtimestamp(reviewTime_val)
            reviewTime_val = reviewTime_val.strftime("%B %d, %Y")
            i["reviewTime"] = reviewTime_val

            # remove unnecessary columns
            del i["unixReviewTime"]
            del i["id"]

        output = {"review": query_result_edited}
        output = json.dumps(output, sort_keys=True, indent=4)

        return output
