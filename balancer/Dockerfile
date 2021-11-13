FROM nginx:alpine@sha256:12aa12ec4a8ca049537dd486044b966b0ba6cd8890c4c900ccb5e7e630e03df0
RUN apk add gettext
COPY ./nginx.conf /etc/nginx/nginx.conf
CMD envsubst '\$DOMAIN' < /etc/nginx/nginx.conf > /etc/nginx/nginx.conf && nginx -g 'daemon off;'
