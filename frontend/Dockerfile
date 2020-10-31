FROM node:lts

RUN mkdir /app
WORKDIR /app

COPY ./app/package.json /app/package.json
COPY ./app/yarn.lock /app/yarn.lock
COPY ./app/node_modules /app/node_modules