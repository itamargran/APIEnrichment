FROM python:3.8

WORKDIR /osm

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY osm/ .

CMD ["python", "./app.py"]
