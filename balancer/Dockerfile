FROM nginx:alpine@sha256:324413aaa0124313462b67808c231b8391ee0c5941c641d3b068e3f6687e2eb1
RUN apk add gettext
COPY ./nginx.conf /etc/nginx/nginx.conf
CMD envsubst '\$DOMAIN' < /etc/nginx/nginx.conf > /etc/nginx/nginx.conf && nginx -g 'daemon off;'
