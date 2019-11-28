touch ./logs/accesslog.log 
chmod 777 ./logs/accesslog.log
pipenv install
pipenv run gunicorn --workers=4 -b 0.0.0.0:80 "app:create_app()"
