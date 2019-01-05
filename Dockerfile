FROM python:3-slim as builder
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y\
    libmariadbclient-dev-compat \
    gcc
WORKDIR /code
COPY requirements/*.txt /code/requirements/
RUN pip install --no-cache-dir pip wheel -U
RUN pip install --no-cache-dir -r requirements/development.txt

FROM builder as dev
VOLUME /code
COPY . /code/

FROM builder
VOLUME /code/media
VOLUME /code/staticfiles
# Copy the code as late as possible.
COPY . /code/
ENTRYPOINT ["sh", "contrib/docker/entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]