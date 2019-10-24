#!/bin/bash

docker-compose start iis-database;
pipenv shell;
sleep 1;
python3 app.py;
