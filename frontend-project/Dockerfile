FROM node:14.16.1-slim@sha256:24f6102188449a6e30b7e779e9e9e6cb940c9b005938dc54ac6bbad5c5647ba7

RUN apt update && apt install -y g++ git make python3

WORKDIR /code

EXPOSE 8000

CMD ["bash", "-c", "yarn && yarn start"]
