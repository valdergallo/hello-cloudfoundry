help:
	@echo "test-uwsgi	run uwsgi server"
	@echo "deploy		send content to CF server"

test-uwsgi:
	uwsgi --http :9090 --wsgi-file hello.py

deploy:
	cf push
