FROM ubuntu:22.04

ENV TZ = "Europe/Warsaw"
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update

RUN apt install -y python3.8

