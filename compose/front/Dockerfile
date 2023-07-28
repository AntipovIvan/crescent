FROM node:18-alpine 

ARG PROJ_DIR=/vue_proj

RUN mkdir -p ${PROJ_DIR}
COPY ./front ${PROJ_DIR}

WORKDIR ${PROJ_DIR}

RUN npm install -g npm

COPY ./front/package.json ${PROJ_DIR}
COPY ./front/package-lock.json ${PROJ_DIR}
RUN npm install

CMD [ "npm", "run", "serve" ]