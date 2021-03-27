FROM node:14.16.0-slim@sha256:9907fcfcef9a8c05ebbaad4fc913e06573d46d2dbcf68c2952f7b777d8d5ca29

RUN apt update && apt install -y g++ git make python3

WORKDIR /code

EXPOSE 8000

CMD ["bash", "-c", "yarn && yarn start"]
