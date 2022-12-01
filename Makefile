run:
flask run -p 8000 -h 0.0.0.0

init:
flask db init

migrate:
flask db migrate

upgrade:
flask db upgrade
