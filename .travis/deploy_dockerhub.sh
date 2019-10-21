docker login --username $DOCKER_USERNAME --password $DOCKER_PASSWORD docker.io
docker build -t juanjelgueta/lmmflask:imagetag .
docker push juanjelgueta/lmmflask:imagetag
