#!/bin/bash

docker container stop throwaway
docker container rm throwaway
docker image build -t throwaway:1.0 -f Dockerfile.setup .
docker container run -d --name throwaway throwaway:1.0
