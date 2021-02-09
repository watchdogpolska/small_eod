FROM node:14.15.4-slim@sha256:4f4e17e43e434774aac4d323b5b1d277028bfc646d3685883fea17ac9286b382

RUN apt update && apt install -y g++ git make python3

WORKDIR /code

EXPOSE 8000

CMD ["bash", "-c", "yarn && yarn start"]
