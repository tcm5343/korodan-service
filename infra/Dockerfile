FROM python:3.13-slim-bookworm

USER root
WORKDIR /work

RUN apt update
RUN apt install -y \
    npm \
    nodejs

ADD ./package.json .
ADD ./package-lock.json .
RUN npm install

ENV PATH=$PATH:/work/node_modules/.bin
ENV PYTHONPATH=$PYTHONPATH:/work/infra/src:/work/infra/test

ENTRYPOINT [ ]
