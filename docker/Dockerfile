FROM ubuntu:20.04

# non interactive
ARG DEBIAN_FRONTEND=noninteractive

# Update
RUN apt update && apt install -y --no-install-recommends \
    apt-utils \

# Python
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3=3.8* \
    python3.8-dev=3.8* \
    python3-pip=20.0.2-5ubuntu1* \
    python3-setuptools=45.2.0-1*

# gcc, avr, etc
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc make \
    gcc-avr avr-libc \
    libelf-dev \
    simavr

# Bazelisk
RUN wget https://github.com/bazelbuild/bazelisk/releases/download/v1.12.0/bazelisk-linux-amd64 -O /usr/bin/bazel \
&& chmod +x /usr/bin/bazel
