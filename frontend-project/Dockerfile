FROM node:14.17.0-slim@sha256:a3ff0656dfa88cc5c4092af3e18d16cbbbf50417ce4d0565d013f9ef51860b3a

RUN apt update && apt install -y g++ git make python3

WORKDIR /code

EXPOSE 8000

CMD ["bash", "-c", "yarn && yarn start"]
