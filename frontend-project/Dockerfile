FROM node:14.15.4-slim@sha256:f386ed4ccc9e07acf595ef3d8d8060326e1ea3010f6603f7e853628f4c99ff03

RUN apt update && apt install -y g++ git make python3

WORKDIR /code

EXPOSE 8000

CMD ["bash", "-c", "yarn && yarn start"]
