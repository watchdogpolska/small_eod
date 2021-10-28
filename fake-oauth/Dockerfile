FROM node:latest@sha256:a562ce5da0b5e43107b4acbc5d8845129370f11bcb81c795601dc3d6004d6158

WORKDIR oauth

# Generate a self signed certificate. This will let us handle https requests.
RUN openssl genrsa -out key.pem
RUN openssl req -new -key key.pem -out csr.pem -batch
RUN openssl x509 -req -days 9999 -in csr.pem -signkey key.pem -out cert.pem
RUN rm csr.pem

COPY server.js ./

EXPOSE 5678

CMD ["node",  "server.js"]
