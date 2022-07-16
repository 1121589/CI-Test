FROM ubuntu:20.04

# non interactive
ARG DEBIAN_FRONTEND=noninteractive

# Update
RUN apt update && apt install -y \
    apt-utils

# gcc, avr, etc
RUN apt-get update && apt-get install -y \
    wget \
    gcc \
    make \
    gcc-avr \
    avr-libc \
    libelf-dev \
    simavr

# Bazelisk
RUN wget https://github.com/bazelbuild/bazelisk/releases/download/v1.12.0/bazelisk-linux-amd64 -O /usr/bin/bazel \
&& chmod +x /usr/bin/bazel
