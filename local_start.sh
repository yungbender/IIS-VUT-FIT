#!/bin/bash

docker-compose start iis-database;
pipenv shell;
python3 app.py;
