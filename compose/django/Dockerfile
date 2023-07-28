# Pull the official base image
FROM python:3.11.4-bookworm

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ARG PROJ_DIR=/my_proj

RUN mkdir -p ${PROJ_DIR}
COPY ./back ${PROJ_DIR}

WORKDIR ${PROJ_DIR}

RUN pip install -U pip \
    pip install -r requirements.txt

COPY ./compose/django/entry.sh /entry.sh
RUN chmod +x /entry.sh
ENTRYPOINT [ "/entry.sh" ]