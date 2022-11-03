FROM python:3.10-slim
RUN mkdir /app
COPY app/requirements/base.txt /app
COPY app/requirements/prod.txt /app
RUN pip3 install -r /app/prod.txt --no-cache-dir
COPY app/ /app
WORKDIR /app
CMD gunicorn src.wsgi:application --bind 0.0.0.0:5000