FROM python:3.8-alpine

WORKDIR /code

RUN pip install --upgrade pip

COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "estadoAnimoMascota.py"]
