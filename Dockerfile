FROM python:3-slim as builder
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y\
    libmariadbclient-dev-compat \
    gcc wait-for-it \
&& rm -rf /var/lib/apt/lists/*
WORKDIR /code
COPY requirements/*.txt /code/requirements/
RUN pip install --no-cache-dir pip wheel -U
RUN pip install --no-cache-dir -r requirements/development.txt

FROM builder

VOLUME /code/media
VOLUME /code/staticfiles
# Copy the code as late as possible.
COPY . /code/
ENTRYPOINT ["sh", "contrib/docker/entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]