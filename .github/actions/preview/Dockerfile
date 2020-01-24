FROM node:10
WORKDIR /src
COPY /package* ./
ENV NODE_ENV=production
RUN npm ci
COPY . .
CMD ["/src/lib/index.js"]
