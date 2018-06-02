FROM python:3-slim as builder
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y\
    libmysqlclient-dev \
    gcc
RUN mkdir /code /code/production
WORKDIR /code
COPY requirements/*.txt /code/requirements/
RUN pip install --no-cache-dir pip wheel -U
RUN pip install --no-cache-dir -r requirements/production.txt

FROM builder as development
ENV DJANGO_SETTINGS_MODULE=small_eod.settings.development
ENV SECRET_KEY=CHANGE_ME
RUN pip install -r requirements/development.txt
# Copy the code as late as possible.
COPY . /code/
ENTRYPOINT ["sh", "contrib/docker/entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8080

FROM builder as production
VOLUME /code/media
# Copy the code as late as possible.
COPY . /code/
ENTRYPOINT ["sh", "contrib/docker/entrypoint.sh"]
CMD ["python", "manage.py", "runserver"]