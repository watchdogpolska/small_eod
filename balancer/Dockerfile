FROM nginx:alpine@sha256:db7973cb238c8e8acea5982c1048b5987e9e4da60d20daeef7301757de97357a
RUN apk add gettext
COPY ./nginx.conf /etc/nginx/nginx.conf
CMD envsubst '\$DOMAIN' < /etc/nginx/nginx.conf > /etc/nginx/nginx.conf && nginx -g 'daemon off;'
