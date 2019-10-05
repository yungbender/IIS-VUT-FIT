#!/bin/bash
while true
do
	python3 app.py &
	inotifywait ./templates/mainpage.html
	pkill python3
done
