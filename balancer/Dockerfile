FROM nginx:alpine@sha256:a54c26eca98b5929210c711b33ea920b5c5f27da7001081d44b363c99aa47793
RUN apk add gettext
COPY ./nginx.conf /etc/nginx/nginx.conf
CMD envsubst '\$DOMAIN' < /etc/nginx/nginx.conf > /etc/nginx/nginx.conf && nginx -g 'daemon off;'
