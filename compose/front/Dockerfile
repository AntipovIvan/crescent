# Dev
FROM node:18-alpine 

ARG PROJ_DIR=/front

RUN mkdir -p ${PROJ_DIR}
COPY ./front ${PROJ_DIR}

WORKDIR ${PROJ_DIR}

RUN npm install -g npm
RUN npm install

CMD [ "npm", "run", "dev" ]


# # Prod
# FROM node:18-alpine 

# ARG PROJ_DIR=/front

# RUN mkdir -p ${PROJ_DIR}

# WORKDIR ${PROJ_DIR}

# COPY ./front/dist ${PROJ_DIR}

# RUN npm install -g serve

# EXPOSE 8080

# CMD [ "serve", "-s", "dist", "-p", "8080" ]