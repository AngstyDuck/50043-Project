from flask import jsonify


def _review_list(asin_number):
    sample_output = [
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
                              }
                        ]
    return jsonify(reviews=sample_output)
