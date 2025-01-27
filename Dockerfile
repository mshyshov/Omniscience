FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

LABEL maintainer="Mykhailo Shyshov <msshyshov@gmail.com>"

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY ./babel  /app/babel

COPY ./static /app/static

COPY ./templates /app/templates

COPY ./main.py /app/main.py

WORKDIR /app

ENV PYTHONPATH=/app

ENTRYPOINT [ "python", "main.py" ]