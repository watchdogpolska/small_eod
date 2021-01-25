FROM node:14.15.4-slim@sha256:4ec1416247273c7318c0351e04ed997dd8c8059fc53c94e6c5a65773a299395f

RUN apt update && apt install -y g++ git make python3

WORKDIR /code

EXPOSE 8000

CMD ["bash", "-c", "yarn && yarn start"]
