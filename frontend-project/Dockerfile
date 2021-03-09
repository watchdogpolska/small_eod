FROM node:14.16.0-slim@sha256:6e88e1de84445d0a52c948f8e14c841f96e684693824e72753f66f2e36661b7a

RUN apt update && apt install -y g++ git make python3

WORKDIR /code

EXPOSE 8000

CMD ["bash", "-c", "yarn && yarn start"]
