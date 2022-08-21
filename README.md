# CI System for Atmega
This repository serves as a testing ground for the implementation of a Uni project based on a Continuous Integration for AVR systems.

# Architecture
Based on github actions, it has two major workflows, one for the general build&test running inside a docker container and another to build this docker image and deploy it to the github registry. 

# Build
All changes automatically trigger a workflow by github actions.
In the workflow it is defined the run of bazel to build the entire `application/` folder.

# Test
All changes automatically trigger a workflow by github actions.
In the workflow it is defined the run of bazel to test the entire `application/` folder.
For testing frameworks simavr and unity is used.

# Bazel
To enable build and testing of the AVR systems, a custom toolchain needed to be implemented, it resides in `toolchain` folder.