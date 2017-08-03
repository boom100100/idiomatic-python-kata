FROM python:3.6

RUN apt-get update

ARG uid=1000
ARG gid=1000
RUN addgroup --gid $gid kata
RUN useradd -m --uid $uid -g kata kata


COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt
ENV PYTHONPATH=/code
WORKDIR /code
