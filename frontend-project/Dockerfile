FROM node:14.16.0-slim@sha256:e8a3dbe7f6d334acfe0365260626d3953073334de4c0fde00f93e8e9e19ed5d5

RUN apt update && apt install -y g++ git make python3

WORKDIR /code

EXPOSE 8000

CMD ["bash", "-c", "yarn && yarn start"]
