#!/bin/bash

docker-compose start iis-database
pipenv run python3 app.py
