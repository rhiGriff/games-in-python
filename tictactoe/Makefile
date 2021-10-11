install:
	pipenv install

lint:
	pipenv run flake8 .

test: 
	PYTHONPATH=`pwd`/app \
	pipenv run python -m pytest -vv -s test

run:
	pipenv run python app/tictactoe.py

