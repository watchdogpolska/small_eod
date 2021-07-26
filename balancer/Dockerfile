FROM nginx:alpine@sha256:ad14f3471c0fd650022d3d2ff370e02c51113679070486e510dfcbe64d00565a
RUN apk add gettext
COPY ./nginx.conf /etc/nginx/nginx.conf
CMD envsubst '\$DOMAIN' < /etc/nginx/nginx.conf > /etc/nginx/nginx.conf && nginx -g 'daemon off;'
