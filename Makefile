MANAGE_PATH = book_exchange/manage.py
DATA_PATH = book_exchange/fixtures/books.json


migrations:
	python $(MANAGE_PATH) makemigrations

migrate: migrations
	python $(MANAGE_PATH) migrate

flush: migrate
	echo yes | python $(MANAGE_PATH) flush

superuser: flush
	python $(MANAGE_PATH) createsuperuser

loaddata: superuser
	python $(MANAGE_PATH) loaddata $(DATA_PATH)

run: loaddata
	python $(MANAGE_PATH) runserver
