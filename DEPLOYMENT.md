# Deploy on Azure

This tutorial is for simple deployment on Azure.

## Docker related steps

### 1st step

Create a docker hub account [here](https://hub.docker.com/) if not already done.

### 2nd step

Build API image as in README.md if not already done.

`docker build -t YOUR_DOCKER_IMAGE_NAME .`

example : `docker build -t generic_api .`

### 3rd step
Log to docker hub with cli

`docker login`

### 4th step
Create dockerhub tag
`docker tag YOUR_DOCKER_IMAGE_NAME YOUR_DOCKER_HUB_USERNAME/YOUR_DOCKER_HUB_REPO`

example : `docker tag generic_api fanchouille/generic_api`

### 5th step
Push image

`docker push YOUR_DOCKER_HUB_USERNAME/YOUR_DOCKER_HUB_REPO`

example : `docker push fanchouille/generic_api`


## Azure related steps

### 1st step
Connect to [Azure](portal.azure.com)

### 2nd step
search for *Web app for containers*

### 3rd step
Choose app name, your will access your api at
https://YOUR_API_NAME.azurewebsites.net

Choose relevant subscription & resource group

### 4th step
Configure container > choose Docker Hub

Put Image name : YOUR_DOCKER_HUB_USERNAME/YOUR_DOCKER_HUB_REPO and apply.

example : fanchouille/generic_api

### 5th step
Create API

Your API documentation is available at [https://YOUR_API_NAME.azurewebsites.net/docs](https://YOUR_API_NAME.azurewebsites.net/docs)