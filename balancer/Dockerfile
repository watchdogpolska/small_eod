FROM nginx:alpine@sha256:581ac1da0f8f8c342fa6cf77885a2320227667c0bc42bdca4b1dd74599d02498
RUN apk add gettext
COPY ./nginx.conf /etc/nginx/nginx.conf
CMD envsubst '\$DOMAIN' < /etc/nginx/nginx.conf > /etc/nginx/nginx.conf && nginx -g 'daemon off;'
