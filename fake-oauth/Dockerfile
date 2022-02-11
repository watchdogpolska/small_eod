FROM node:latest@sha256:a0590a265b222387d756ba357c4a9875778f1a7638ac011f3fb4942d3b7ae5c0

WORKDIR oauth

# Generate a self signed certificate. This will let us handle https requests.
RUN openssl genrsa -out key.pem
RUN openssl req -new -key key.pem -out csr.pem -batch
RUN openssl x509 -req -days 9999 -in csr.pem -signkey key.pem -out cert.pem
RUN rm csr.pem

COPY server.js ./

EXPOSE 5678

CMD ["node",  "server.js"]
