FROM nginx:alpine@sha256:ba39aed615e51956312a345837b6316681504fb52452edc0e9f671fd88472dc5
RUN apk add gettext
COPY ./nginx.conf /etc/nginx/nginx.conf
CMD envsubst '\$DOMAIN' < /etc/nginx/nginx.conf > /etc/nginx/nginx.conf && nginx -g 'daemon off;'
