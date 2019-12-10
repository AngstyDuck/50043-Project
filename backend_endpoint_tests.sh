#!/bin/bash

# [GET] /single_book/<asin>
curl -X GET 127.0.0.1:5000/single_book/B00J4PUJ8U

# [GET] /main_top_row_books
curl -X GET 127.0.0.1:5000/main_top_row_books

# [GET] /main_bot_row_books
curl -X GET '127.0.0.1:5000/main_bot_row_books?start_list=1&end_list=20&seed=0'

# [PUT] /helpful_review
curl -X PUT -d '{"reviewerID": "A3DE6XGZ2EPADS","asin": "B000F83SZQ","reviewerName": "WPY"}' -H "Content-Type: application/json" 127.0.0.1:5000/helpful_review

# [GET] /categories
curl -X GET 127.0.0.1:5000/categories

# [GET] /search_books
curl -X GET '127.0.0.1:5000/search_books?start_list=0&end_list=20&searchtext=stand&filtertext='

# [GET] /filter_books
curl -X GET '127.0.0.1:5000/filter_books?start_list=0&end_list=20&filtertext=accessories'

# [GET] /review_list/<asin>
curl -X GET 127.0.0.1:5000/review_list/B000F83SZQ

# [POST] /post_new_review
curl -d '{"asin":"asin_value", "overall":5, "reviewText":"oh hey ;)", "reviewerName":"ur m0m", "summary":"yes"}' -H "Content-Type: application/json" -X POST http://localhost:5000/post_new_review

