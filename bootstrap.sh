#!/bin/sh
export FLASK_APP=./planA-infos/app.py
source $(pipenv --venv)/bin/activate
flask run -h 0.0.0.0

