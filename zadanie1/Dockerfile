FROM ubuntu:22.04

ENV TZ="Europe/Warsaw"
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update

RUN apt install -y python3.8

RUN apt-get install -y openjdk-8-jdk kotlin

RUN apt-get update && \
    apt-get install -y wget && \
    wget -q https://services.gradle.org/distributions/gradle-8.6-bin.zip -P /tmp && \
    unzip -q /tmp/gradle-8.6-bin.zip -d /opt && \
    rm /tmp/gradle-8.6-bin.zip

ENV PATH="${PATH}:/opt/gradle/gradle-8.6/bin"
