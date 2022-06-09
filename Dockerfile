FROM node:16.14.2

# Create app directory
WORKDIR /usr/src/app

COPY package.json ./

RUN npm install

COPY . .

EXPOSE 8181

CMD [ "node", "server.js" ]