#!/bin/bash

# [GET] /single_book/<asin>

# [GET] /main_top_row_books
curl -X GET 127.0.0.1:5000/main_top_row_books

# [GET] /main_bot_row_books
curl -X GET "127.0.0.1:5000/main_bot_row_books?start_list=1&seed=0"

# [PUT] /helpful_review

# [GET] /review_list/<asin_number>
curl -X GET -d "asin_number=B000F83SZQ" 127.0.0.1:5000/review_list

# [POST] /post_new_review
curl -d '{"asin":"asin_value", "overall":5, "reviewText":"oh hey ;)", "reviewerName":"ur m0m", "summary":"yes"}' -H "Content-Type: application/json" -X POST http://localhost:5000/post_new_review

