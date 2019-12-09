#!/bin/bash

docker container stop throwaway
docker container rm throwaway
docker image build -t throwaway:1.0 .
docker container run --name throwaway -p 5000:5000 throwaway:1.0
