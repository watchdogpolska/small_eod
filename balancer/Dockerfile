FROM nginx:alpine@sha256:44e208ac2000daeff77c27a409d1794d6bbdf52067de627c2da13e36c7d59582
RUN apk add gettext
COPY ./nginx.conf /etc/nginx/nginx.conf
CMD envsubst '\$DOMAIN' < /etc/nginx/nginx.conf > /etc/nginx/nginx.conf && nginx -g 'daemon off;'
