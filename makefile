
up-dev:
	docker-compose --env-file .env.dev -f docker-compose-dev.yml up -d --no-deps --build

down-dev:
	docker-compose --env-file .env.dev -f docker-compose-dev.yml down


build:
	docker-compose --env-file .env -f docker-compose.yml up -d  --no-deps --build

migrate:
	docker-compose --env-file .env -f docker-compose.yml exec -T server python manage.py migrate --noinput

collectstatic:
	docker-compose --env-file .env -f docker-compose.yml exec -T server python manage.py collectstatic --no-input --clear


up-prod:
	make build
	make migrate
	make collectstatic

down-prod:
	docker-compose --env-file .env -f docker-compose.yml down