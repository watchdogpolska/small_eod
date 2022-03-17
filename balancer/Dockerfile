FROM nginx:alpine@sha256:1e18d60ec3e83a1a01f07457ba6ce045fd3cb65ad1c2bbbb07beb62cc3037543
RUN apk add gettext
COPY ./nginx.conf /etc/nginx/nginx.conf
CMD envsubst '\$DOMAIN' < /etc/nginx/nginx.conf > /etc/nginx/nginx.conf && nginx -g 'daemon off;'
