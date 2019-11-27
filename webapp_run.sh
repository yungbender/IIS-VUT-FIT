touch ./logs/accesslog.log 
chmod 777 ./logs/accesslog.log
pipenv install
pipenv run gunicorn --access-logfile ./logs/accesslog.log --log-level info --workers=4 -b 0.0.0.0:6969 "app:create_app()"
