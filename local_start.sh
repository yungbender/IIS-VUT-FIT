#!/bin/bash

docker-compose start iis-database
pipenv install
pipenv run python3 app.py