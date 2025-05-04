#!/bin/bash

docker build -t brayand/microservice-example-simple:0.1.0 . --no-cache

docker push brayand/microservice-example-simple:0.1.0