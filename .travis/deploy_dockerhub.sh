docker build -t juanjelgueta/lmmflask:imagetag .
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker push juanjelgueta/lmmflask:imagetag
