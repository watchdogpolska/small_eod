FROM node:14.15.0-slim@sha256:72ab6546194fdf2f96c5abc22e2b5b819eddda505c1fba26ef62705b867a1320

RUN apt update && apt install -y g++ git make python3

WORKDIR /code

EXPOSE 8000

CMD ["bash", "-c", "yarn && yarn start"]
