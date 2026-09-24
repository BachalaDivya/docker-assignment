FROM node:18-alpine

WORKDIR /app

COPY package.json .

RUN npm install

COPY app.js .

EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=5s CMD wget --spider http://localhost:3000 || exit 1

CMD ["npm", "start"]
