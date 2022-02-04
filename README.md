### Installaton:

```
## install required module
pip install -r requirements.txt

## create db file
python manage.py makemigrations
python manage.py migrate

## run
python manage.py runserver

```

### Using Docker

```
docker build  -t django-task .

docker run -d -it -p 8000:8000 --name django-task-wobot django-task
```