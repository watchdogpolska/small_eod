FROM nginx:alpine@sha256:8df2c57b2b9ba34ac4df6e8f643a958ef94b9396c30326f95a0f0206808e9382
RUN apk add gettext
COPY ./nginx.conf /etc/nginx/nginx.conf
CMD envsubst '\$DOMAIN' < /etc/nginx/nginx.conf > /etc/nginx/nginx.conf && nginx -g 'daemon off;'
