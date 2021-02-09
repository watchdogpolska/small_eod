FROM node:14.15.4-slim@sha256:9b99c02061bdf7899e28e22efd0ef8f6e394b69a638a0a6a6b088e381e730794

RUN apt update && apt install -y g++ git make python3

WORKDIR /code

EXPOSE 8000

CMD ["bash", "-c", "yarn && yarn start"]
