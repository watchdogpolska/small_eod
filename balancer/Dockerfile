FROM nginx:alpine@sha256:1c5711ad6eb3324dde0c429a6add14607b16b158d5bd44e026ae197969e5fc1f
RUN apk add gettext
COPY ./nginx.conf /etc/nginx/nginx.conf
CMD envsubst '\$DOMAIN' < /etc/nginx/nginx.conf > /etc/nginx/nginx.conf && nginx -g 'daemon off;'
