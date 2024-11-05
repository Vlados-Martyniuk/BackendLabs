FROM python:3.11.3-slim-bullseye

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /app

ENV FLASK_APP=app.views:app

CMD flask run --host=0.0.0.0 --port=$PORT
