FROM nginx:alpine@sha256:f01a7a92c6b7ab134b3a924a0c9b0b487bfb890d1563773fefc2229ce55e4ca3
RUN apk add gettext
COPY ./nginx.conf /etc/nginx/nginx.conf
CMD envsubst '\$DOMAIN' < /etc/nginx/nginx.conf > /etc/nginx/nginx.conf && nginx -g 'daemon off;'
