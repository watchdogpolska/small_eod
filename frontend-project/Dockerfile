FROM node:14.15.3-slim@sha256:2a9c12b10d34bcf880d303500a9262359b6ee096f08aa73215c865b3df3a23a3

RUN apt update && apt install -y g++ git make python3

WORKDIR /code

EXPOSE 8000

CMD ["bash", "-c", "yarn && yarn start"]
