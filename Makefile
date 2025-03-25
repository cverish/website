venv:
	python3 -m venv .venv

freeze:
	.venv/bin/pip freeze >> requirements.txt

init: venv
	.venv/bin/pip install -r requirements.txt
	npm install

runserver:
	.venv/bin/python manage.py runserver

tailwindbuild:
	npx tailwindcss build -i ./static/css/main.css -o ./static/css/output.css

tailwindwatch:
	npx tailwindcss build -i ./static/css/main.css -o ./static/css/output.css -w

format:
	npx rustywind --write .
	.venv/bin/python -m djlint . --reformat
	.venv/bin/ruff format

lint:
	npx rustywind .
	.venv/bin/python -m djlint . --lint
	.venv/bin/ruff check

bake: tailwindbuild
	DEBUG=False .venv/bin/python manage.py build

bakeserver: tailwindbuild
	.venv/bin/python manage.py buildserver
