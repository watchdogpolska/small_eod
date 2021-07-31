FROM nginx:alpine@sha256:1b68400cbeec3d5334edcb8606b2ac4badc9b0401cc209e8941853aec332efea
RUN apk add gettext
COPY ./nginx.conf /etc/nginx/nginx.conf
CMD envsubst '\$DOMAIN' < /etc/nginx/nginx.conf > /etc/nginx/nginx.conf && nginx -g 'daemon off;'
