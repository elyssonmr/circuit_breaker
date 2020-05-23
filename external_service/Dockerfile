FROM python:3.7-alpine

EXPOSE 5000

RUN mkdir -p /usr/app
WORKDIR /usr/app

COPY . /usr/app

RUN pip install -r requirements.txt

CMD gunicorn -w 4 --threads 4 -b 0.0.0.0:5000 app:app
