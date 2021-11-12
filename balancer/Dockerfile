FROM nginx:alpine@sha256:b5e5afb5ebd67dbf16d885644600694b43b61a20ea68c6df13a031b3c1fb8365
RUN apk add gettext
COPY ./nginx.conf /etc/nginx/nginx.conf
CMD envsubst '\$DOMAIN' < /etc/nginx/nginx.conf > /etc/nginx/nginx.conf && nginx -g 'daemon off;'
