FROM nginx:alpine@sha256:89a804b22327400a6358dcc422844272b993c57d30ec50a3cb6cc2a0a8e4d1b1
RUN apk add gettext
COPY ./nginx.conf /etc/nginx/nginx.conf
CMD envsubst '\$DOMAIN' < /etc/nginx/nginx.conf > /etc/nginx/nginx.conf && nginx -g 'daemon off;'
