FROM node:16.8.0-slim@sha256:441afc10bb9f886fb6dabdf20458743273dd73e51fe9ea39db39a1b4a20124fe AS env

RUN apt update && apt install -y g++ git make python3
WORKDIR /code

# PRODUCTION BUILD
FROM env AS builder
COPY ./ /code
RUN yarn && yarn build

FROM nginx:stable-alpine@sha256:1173fbfbbffd6e8a975a9a5a31edd4409b78d11fdc5e67985e13ea2dea915290 AS prod
COPY ./nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /code/dist /usr/share/nginx/html
EXPOSE 8000
CMD ["nginx", "-g", "daemon off;"]

# DEVELOPMENT BUILD
FROM env
CMD ["bash", "-c", "yarn && yarn start"]
