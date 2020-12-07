FROM python:3.8

WORKDIR /src

COPY . /src

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "osm/app.py"]
