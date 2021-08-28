FROM nginx:alpine@sha256:859ec6f2dc548cd2e5144b7856f2b5c37b23bd061c0c93cfa41fb5fb78307ead
RUN apk add gettext
COPY ./nginx.conf /etc/nginx/nginx.conf
CMD envsubst '\$DOMAIN' < /etc/nginx/nginx.conf > /etc/nginx/nginx.conf && nginx -g 'daemon off;'
