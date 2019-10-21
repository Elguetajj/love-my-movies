docker build -t juanjelgueta/lmmflask:imagetag .
docker login --username $DOCKER_USERNAME --password $DOCKER_PASSWORD docker.io
docker push juanjelgueta/lmmflask:imagetag
