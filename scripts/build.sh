#!/bin/sh

docker build -t pyhawaii-web --build-arg TAG=$(git rev-parse HEAD) -f scripts/containerize/Dockerfile .
