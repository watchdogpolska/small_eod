FROM node:12-alpine
WORKDIR /src
COPY package* ./
ENV NODE_ENV=production
RUN npm ci
COPY . .
CMD ["node","index.js"]
