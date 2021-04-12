FROM node:14.16.1-slim@sha256:027ca5b035e85229e96ebd4e60c26386126e6a208f238561759b3d68ac50cae9

RUN apt update && apt install -y g++ git make python3

WORKDIR /code

EXPOSE 8000

CMD ["bash", "-c", "yarn && yarn start"]
