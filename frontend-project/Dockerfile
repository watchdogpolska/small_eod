FROM node:14.16.1-slim@sha256:58dbfbdf664f703072bd8263b787301614579c8e345029cdc3d9acf682e853a9

RUN apt update && apt install -y g++ git make python3

WORKDIR /code

EXPOSE 8000

CMD ["bash", "-c", "yarn && yarn start"]
