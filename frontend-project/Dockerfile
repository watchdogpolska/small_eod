FROM node:14.16.0-slim@sha256:7ff9cf5e411481ee734479637265f063c5f356f496d0f9c47112312cb7b46d42

RUN apt update && apt install -y g++ git make python3

WORKDIR /code

EXPOSE 8000

CMD ["bash", "-c", "yarn && yarn start"]
