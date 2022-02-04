FROM python:3.7-slim

COPY requirements.txt /app/

RUN pip install -r /app/requirements.txt

COPY . /app/

WORKDIR /app

RUN python3 manage.py makemigrations && python3 manage.py migrate

CMD [ "python3","manage.py","runserver" ,"0.0.0.0:8000"]