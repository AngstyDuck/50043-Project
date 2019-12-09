from flask import request, url_for, jsonify, Blueprint
from flask_api import FlaskAPI, status, exceptions

# local modules
import sys
import os
dirname = os.path.dirname(__file__)
sys.path.insert(1, dirname)
#from main_bot_row_books import _main_bot_row_books
from single_book import _single_book
from main_bot_row_books import _main_bot_row_books
from main_bot_row_books import _main_top_row_books
# from single_book import _single_book
from helpful_review import _helpful_review
from main_top_row_books import _main_top_row_books
from categories import _categories
from filter_books import _filter_books
from search_books import _search_books

module = Blueprint("books", __name__)


def _test():
    return jsonify({"test message": "hello"})


#module.add_url_rule("/main_bot_row_books/<start>/<seed>", view_func=_main_bot_row_books, methods=["GET"])
module.add_url_rule("/single_book/<asin>", view_func=_single_book, methods=["GET"])
module.add_url_rule("/main_top_row_books", view_func=_main_top_row_books, methods=["GET"])
module.add_url_rule("/main_bot_row_books", view_func=_main_bot_row_books, methods=["GET"])
#module.add_url_rule("/single_book/<asin>", view_func=_single_book, methods=["GET"])
module.add_url_rule("/test", view_func=_test, methods=["GET"])
module.add_url_rule("/helpful_review", view_func=_helpful_review, methods=["PUT"])
module.add_url_rule("/main_top_row_books", view_func=_main_top_row_books, methods=["GET"])
module.add_url_rule("/categories", view_func=_categories, methods=["GET"])
module.add_url_rule("/filter_books", view_func=_filter_books, methods=["GET"])
module.add_url_rule("/search_books", view_func=_search_books, methods=["GET"])
