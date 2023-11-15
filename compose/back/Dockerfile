FROM python:3.11.4-bookworm

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ARG PROJ_DIR=/back

RUN mkdir -p ${PROJ_DIR}
COPY ./back ${PROJ_DIR}

WORKDIR ${PROJ_DIR}

RUN pip install -U pip \
    pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:7000", "--insecure"]
