FROM node:12-slim

RUN apt update && apt install -y g++ git make python3

WORKDIR /code

EXPOSE 8000

CMD ["bash", "-c", "yarn && yarn start"]
