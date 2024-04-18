FROM python:3.9-slim-buster

WORKDIR /app
COPY requirements.txt . 
RUN pip install --prefer-binary -r requirements.txt
COPY . .

CMD python manage.py runserver 0.0.0.0:80