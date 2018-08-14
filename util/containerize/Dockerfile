FROM python:2.7.15-alpine3.8

RUN apk update \
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev \
  && pip install psycopg2-binary==2.7.5 \
  && apk del build-deps gcc python3-dev musl-dev


# environment

ENV PYTHONPATH=/usr/site/apps:/usr/site/vendor DJANGO_SETTINGS_MODULE=config.settings.heroku
WORKDIR /usr/site


# python requirements

COPY ./util/containerize/requirements.txt ./
RUN pip install -r requirements.txt


# copy site

COPY ./site/ ./


# collect static files into single directory

COPY ./util/containerize/env.collectstatic ./env.collectstatic
RUN DJANGO_ENVFILE_PATH=/usr/site/env.collectstatic \
    python manage.py collectstatic -v 0 --no-input && rm /usr/site/env.collectstatic


# set up run-as user

RUN adduser -D app
USER app


# tag the container

ARG TAG
ENV CONTAINER_TAG=$TAG


# execute app context

CMD gunicorn config.wsgi --bind 0.0.0.0:8000 -w 2 -k gevent
