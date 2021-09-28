FROM node:latest@sha256:c33a8221330d87a2113fb6cdbb8fbb243592c62f89de923e9ef5bb8b627c2b9d

WORKDIR oauth

# Generate a self signed certificate. This will let us handle https requests.
RUN openssl genrsa -out key.pem
RUN openssl req -new -key key.pem -out csr.pem -batch
RUN openssl x509 -req -days 9999 -in csr.pem -signkey key.pem -out cert.pem
RUN rm csr.pem

COPY server.js ./

EXPOSE 5678

CMD ["node",  "server.js"]
