FROM node:latest@sha256:7955e50cb7e48d7f6240c785827989ef405a7e428ced1958b8b5b6a64daf96b7

WORKDIR oauth

# Generate a self signed certificate. This will let us handle https requests.
RUN openssl genrsa -out key.pem
RUN openssl req -new -key key.pem -out csr.pem -batch
RUN openssl x509 -req -days 9999 -in csr.pem -signkey key.pem -out cert.pem
RUN rm csr.pem

COPY server.js ./

EXPOSE 5678

CMD ["node",  "server.js"]
