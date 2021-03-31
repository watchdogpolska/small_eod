FROM node:14.16.0-slim@sha256:fcb9b40c55b2827442f80ee39cf709279d54636acf134bc7075adae045588e92

RUN apt update && apt install -y g++ git make python3

WORKDIR /code

EXPOSE 8000

CMD ["bash", "-c", "yarn && yarn start"]
