FROM python:3.12-alpine

WORKDIR /code
RUN pip install --upgrade pip
COPY ./requirements.txt /requirements.txt
COPY . .
RUN pip install -r /requirements.txt

COPY ./scripts /scripts/
RUN chmod +x /scripts/*
RUN apk add --no-cache dos2unix
RUN dos2unix /scripts/entrypoint.sh

CMD ["sh", "/scripts/entrypoint.sh"]

