FROM nginx:alpine@sha256:bbb6a604aac1496ed0239ab1a5180394838de57ba0540eb96a32748f5895400e
RUN apk add gettext
COPY ./nginx.conf /etc/nginx/nginx.conf
CMD envsubst '\$DOMAIN' < /etc/nginx/nginx.conf > /etc/nginx/nginx.conf && nginx -g 'daemon off;'
