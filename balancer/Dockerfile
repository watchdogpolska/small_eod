FROM nginx:alpine@sha256:053f34bb2b114d3cd2dc4dc0790233eb3d14612e7e6d17a1816003405023e215
RUN apk add gettext
COPY ./nginx.conf /etc/nginx/nginx.conf
CMD envsubst '\$DOMAIN' < /etc/nginx/nginx.conf > /etc/nginx/nginx.conf && nginx -g 'daemon off;'
