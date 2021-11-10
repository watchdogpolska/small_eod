FROM nginx:alpine@sha256:99a391b906f1c8d16122d0b6d290997df576b17d67de0ba18af6690f9c01ff47
RUN apk add gettext
COPY ./nginx.conf /etc/nginx/nginx.conf
CMD envsubst '\$DOMAIN' < /etc/nginx/nginx.conf > /etc/nginx/nginx.conf && nginx -g 'daemon off;'
