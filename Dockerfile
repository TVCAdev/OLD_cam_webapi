FROM python:latest

ENV TOP_DIR /cam_webapi

RUN mkdir ${TOP_DIR}

COPY camera.py ${TOP_DIR}

WORKDIR ${TOP_DIR}
RUN apt-get update && apt-get install -y \
    v4l-utils \
    libopencv-dev \
    python3-opencv \
    python3-flask

CMD ["/usr/bin/python3","camera.py"]

