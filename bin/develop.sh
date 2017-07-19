#!/bin/bash
# Start developemnt server on :8000
set -x

export DOCKER_CONFIG=${DOCKER_CONFIG:-docker-compose.yml}
docker-compose -f $DOCKER_CONFIG build
./bin/init_db.sh
docker-compose -f $DOCKER_CONFIG run --rm django migrate
docker-compose -f $DOCKER_CONFIG up
