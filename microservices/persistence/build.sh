#!/bin/bash

docker build -t brayand/microservice-example-persistence:0.1.0 . --no-cache

docker push brayand/microservice-example-persistence:0.1.0