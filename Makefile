build:
	docker-compose build
start:
	docker-compose up -d

stop:
	docker-compose stop

down:
	docker-compose down

rebuild: down build start