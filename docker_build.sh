#!/bin/bash
# Build Docker image
set -e
export IMAGE_TAG="fongshway/flask-by-example:develop"
export REQUIREMENTS_INSTALL_CMD="${REQUIREMENTS_INSTALL_CMD:-pipenv install --dev --deploy --system}"

while getopts t: option; do
    case "${option}" in
        t) IMAGE_TAG=${OPTARG}
           echo "-t was set, Parameter: ${OPTARG}"
           ;;
    esac
done

docker build \
    --build-arg REQUIREMENTS_INSTALL_CMD="${REQUIREMENTS_INSTALL_CMD}" \
    --no-cache \
    --force-rm \
    --label flask-by-example \
    --tag ${IMAGE_TAG} .
