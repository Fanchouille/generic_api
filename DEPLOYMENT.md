# Deploy on Azure

This tutorial is for simple deployment on Azure.

## Docker related steps

1. Create a docker hub account [here](https://hub.docker.com/) if not already done.
2. Build API image as in README.md if not already done.

    `docker build -t YOUR_DOCKER_IMAGE_NAME .`

    example : `docker build -t generic_api .`

3. Log to docker hub with cli
    
    `docker login`

4. Create dockerhub tag

    `docker tag YOUR_DOCKER_IMAGE_NAME YOUR_DOCKER_HUB_USERNAME/YOUR_DOCKER_HUB_REPO`

    example : `docker tag generic_api fanchouille/generic_api`

5. Push image

    `docker push YOUR_DOCKER_HUB_USERNAME/YOUR_DOCKER_HUB_REPO`

    example : `docker push fanchouille/generic_api`

## Azure related steps

1. Connect to [Azure](portal.azure.com)
2. Search for *Web app for containers*
3. Choose app name : YOUR_APP_NAME

    you will access your api at https://YOUR_APP_NAME.azurewebsites.net

    Choose relevant subscription & resource group

4. Configure container > choose Docker Hub

    Put Image name : YOUR_DOCKER_HUB_USERNAME/YOUR_DOCKER_HUB_REPO and apply.

    example : fanchouille/generic_api

5. Create API

    Wait for 5 minutes.
    
    Your API is up and documentation is available at [https://YOUR_APP_NAME.azurewebsites.net/docs](https://YOUR_APP_NAME.azurewebsites.net/docs)