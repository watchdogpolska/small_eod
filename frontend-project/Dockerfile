FROM node:12-slim@sha256:012427c4dba7a773c625539d66bbe78e7b2b4672354da34ae45109d699eb7df7

RUN apt update && apt install -y g++ git make python3

WORKDIR /code

EXPOSE 8000

CMD ["bash", "-c", "yarn && yarn start"]
