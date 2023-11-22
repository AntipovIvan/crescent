docker-compose down -v

docker-compose -f docker-compose.prod.yml up --build
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser

Backups:
docker exec <cont> pg_dump -U crescent crescent_prod > backup.sql

If file .sh is not found:
switch from CRLF to LF
