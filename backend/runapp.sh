#!/bin/bash

source venvBackend/bin/activate
export FLASK_APP=wsgi.py
export FLASK_ENV=local
python3 -m flask run --port=5000
