#!/bin/bash

docker build -t brayand/microservice-example-jaeger:0.1.0 . --no-cache

docker push brayand/microservice-example-jaeger:0.1.0