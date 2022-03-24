FROM nginx:alpine@sha256:250c11e0c39dc17ba617f3eb0b28b6f456d46483f04823154c6aa68c432ded72
RUN apk add gettext
COPY ./nginx.conf /etc/nginx/nginx.conf
CMD envsubst '\$DOMAIN' < /etc/nginx/nginx.conf > /etc/nginx/nginx.conf && nginx -g 'daemon off;'
