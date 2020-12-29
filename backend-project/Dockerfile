ARG PYTHON_VERSION="3.7"
FROM python:${PYTHON_VERSION}-slim as builder
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y \
    gcc \
    wait-for-it \
    gettext \
    make \
    && rm -rf /var/lib/apt/lists/*
# make - required for docs build
# wait-for-it - required for dependencies waiting eg. wait to database start
# gcc - for required for some python
# gettext - regenerate locales

WORKDIR /code
COPY requirements/*.txt /code/requirements/
RUN pip install --no-cache-dir pip wheel -U

VOLUME /code/media
VOLUME /code/static
EXPOSE 8000

# PRODUCTION SETTINGS
FROM builder AS prod_settings
ENV DJANGO_SETTINGS_MODULE="config.settings.production"
ENV REQS_FILE="requirements/production.txt"

# DEVELOPMENT SETTINGS
FROM builder AS dev_settings
ENV DJANGO_SETTINGS_MODULE="config.settings.development"
ENV REQS_FILE="requirements/development.txt"

# PRODUCTION BUILD
FROM prod_settings AS prod
RUN pip install --no-cache-dir -r $REQS_FILE
COPY . /code/
CMD ["bash", "-c", "python manage.py collectstatic --no-input && wait-for-it db:5432 && python manage.py migrate && gunicorn -w 3 -b 0.0.0.0:8000 --forwarded-allow-ips='nginx' config.wsgi"]

# DEVELOPMENT BUILD
FROM dev_settings AS dev
# Add git required by coveralls
RUN pip install --no-cache-dir -r $REQS_FILE
COPY . /code/
CMD ["bash", "-c", "python manage.py collectstatic --no-input && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
