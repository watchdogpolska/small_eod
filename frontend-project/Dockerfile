FROM node:14.17.3-slim@sha256:0a89b910e8748253937adec663b169764eb296aea30b696a10f049af95ea223b AS env

RUN apt update && apt install -y g++ git make python3
WORKDIR /code

# PRODUCTION BUILD
FROM env AS builder
COPY ./ /code
RUN yarn && yarn build

FROM nginx:stable-alpine@sha256:bac218df22fef66a173cfa65d0dfa0acca80a3a39df41665be742596977b6c7c AS prod
COPY ./nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /code/dist /usr/share/nginx/html
EXPOSE 8000
CMD ["nginx", "-g", "daemon off;"]

# DEVELOPMENT BUILD
FROM env
CMD ["bash", "-c", "yarn && yarn start"]
