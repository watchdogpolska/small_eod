FROM node:latest@sha256:32fa97f3363975684b08bf4e8a68a47c7905175cc20275b50b974bbd02aba731

WORKDIR oauth

# Generate a self signed certificate. This will let us handle https requests.
RUN openssl genrsa -out key.pem
RUN openssl req -new -key key.pem -out csr.pem -batch
RUN openssl x509 -req -days 9999 -in csr.pem -signkey key.pem -out cert.pem
RUN rm csr.pem

COPY server.js ./

EXPOSE 5678

CMD ["node",  "server.js"]
