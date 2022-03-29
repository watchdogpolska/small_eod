FROM node:16.10.0-slim@sha256:283d85e5a64183046abad478f5f98428720c1b30a72cc11d0cd1cedc1cb53493 AS env

RUN apt update && apt install -y g++ git make python3
WORKDIR /code

# PRODUCTION BUILD
FROM env AS builder
COPY ./ /code
RUN yarn && yarn build

FROM nginx:stable-alpine@sha256:762d45de15352a2a65c54cc4748d8d57f7f7be987920b7cb16b1623c9c5c08e6 AS prod
COPY ./nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /code/dist /usr/share/nginx/html
EXPOSE 8000
CMD ["nginx", "-g", "daemon off;"]

# DEVELOPMENT BUILD
FROM env
CMD ["bash", "-c", "yarn && yarn start"]
