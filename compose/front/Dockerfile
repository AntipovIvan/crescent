FROM node:18-alpine 

ARG PROJ_DIR=/vue_proj

RUN mkdir -p ${PROJ_DIR}
COPY ./front ${PROJ_DIR}

WORKDIR ${PROJ_DIR}

COPY ./front/package.json ${PROJ_DIR}
COPY ./front/package-lock.json ${PROJ_DIR}

# Install Vue CLI globally
RUN npm install -g @vue/cli
RUN npm install @vue/cli
RUN npm install -g npm
RUN npm install

CMD [ "npm", "run", "serve" ]