FROM node:14.17.3-slim@sha256:0a89b910e8748253937adec663b169764eb296aea30b696a10f049af95ea223b

RUN apt update && apt install -y g++ git make python3

WORKDIR /code

EXPOSE 8000

CMD ["bash", "-c", "yarn && yarn start"]
