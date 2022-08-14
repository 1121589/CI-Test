FROM ubuntu:20.04

# non interactive
ARG DEBIAN_FRONTEND=noninteractive

# Update
RUN apt update && apt install -y \
    apt-utils \
    build-essential

# gcc, avr, etc
RUN apt-get update && apt-get install -y \
    wget \
    gcc \
    make \
    gcc-avr \
    avr-libc \
    libelf-dev \
    simavr

RUN apt-get install -y python3

# Bazelisk
RUN wget https://github.com/bazelbuild/bazelisk/releases/download/v1.12.0/bazelisk-linux-amd64 -O /usr/bin/bazel \
&& chmod +x /usr/bin/bazel

# Forçar Bazelisk a dar cache de algumas versões
RUN export USE_BAZEL_VERSION=5.1.1 && bazel --version
RUN export USE_BAZEL_VERSION=latest && bazel --version