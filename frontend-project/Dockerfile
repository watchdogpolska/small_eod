FROM node:14.15.1-slim@sha256:f71ec6638232d39ba7bd1096444e2c4d7ee50e100d6dd1d6a82b8120f469e943

RUN apt update && apt install -y g++ git make python3

WORKDIR /code

EXPOSE 8000

CMD ["bash", "-c", "yarn && yarn start"]
