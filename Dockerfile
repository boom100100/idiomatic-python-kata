FROM python:3.6

RUN apt-get update

ARG uid=1000
ARG gid=1000
RUN addgroup --gid $gid kata
RUN useradd -m --uid $uid -g kata kata


COPY requirements.txt /code/requirements.txt
COPY tests /code/tests
COPY kata /code/kata
COPY linter.cfg /code
RUN pip install --upgrade pip
RUN pip install -r /code/requirements.txt
ENV PYTHONPATH=/code
WORKDIR /code
