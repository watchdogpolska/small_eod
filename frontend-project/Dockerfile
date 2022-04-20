FROM node:17.9.0-slim@sha256:5e83a74abf8eda6d5044127ebc6aa593bf3363d42ed676e915e9ba2c8e05ae63 AS env

RUN apt update && apt install -y g++ git make python3
WORKDIR /code

# PRODUCTION BUILD
FROM env AS builder
COPY ./ /code
RUN yarn && yarn build

FROM nginx:stable-alpine@sha256:ff557e536e5c697c5a28db13ab81bdf9b0c6a20161aa0a46419b9b251872c7df AS prod
COPY ./nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /code/dist /usr/share/nginx/html
EXPOSE 8000
CMD ["nginx", "-g", "daemon off;"]

# DEVELOPMENT BUILD
FROM env
CMD ["bash", "-c", "yarn && yarn start"]
