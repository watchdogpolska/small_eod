FROM nginx:alpine@sha256:77cc350019d0188d3115084265483dcefdd8489ccf719ff4e4c956b48de8ff6a
RUN apk add gettext
COPY ./nginx.conf /etc/nginx/nginx.conf
CMD envsubst '\$DOMAIN' < /etc/nginx/nginx.conf > /etc/nginx/nginx.conf && nginx -g 'daemon off;'
