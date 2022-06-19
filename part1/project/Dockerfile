FROM python:3.10.5-alpine3.16

WORKDIR /app

COPY .  .

RUN pip3 install -r requirements.txt

ENV PORT=5000

CMD gunicorn app:app --bind 0.0.0.0:$PORT