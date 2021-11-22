FROM node:16.9.1-slim@sha256:af6f241029c4d63107c6ccbbd030c44d331786d724bd9c2e615edf46deab58e2 AS env

RUN apt update && apt install -y g++ git make python3
WORKDIR /code

# DEVELOPMENT BUILD
FROM env
CMD ["bash", "-c", "yarn && yarn start"]

# PRODUCTION BUILD
FROM env AS builder
COPY ./ /code
RUN yarn && yarn build

FROM nginx:stable-alpine@sha256:2012644549052fa07c43b0d19f320c871a25e105d0b23e33645e4f1bcf8fcd97 AS prod
COPY ./nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /code/dist /usr/share/nginx/html
EXPOSE 8000
CMD ["nginx", "-g", "daemon off;"]

