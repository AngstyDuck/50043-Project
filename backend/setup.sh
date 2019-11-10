#!/bin/bash

docker container stop throwaway
docker container rm throwaway
docker image build -t throwaway:1.0 .
docker container run --name throwaway throwaway:1.0
