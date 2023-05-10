# Deploying Databricks Dolly 2.0 on Azure Functions

<h3 align="right">Colby T. Ford, Ph.D.</h3>

This repo contains the Docker image and logic for running Databricks Dolly 2.0 model on Azure Functions.

Companion repo for the _[Deploying Databricks Dolly as an API on Azure Functions](https://colbyford.medium.com/deploying-databricks-dolly-on-azure-functions-fac718842d64)_ blog post on Medium.

## Pull the Pre-Built 3B Docker Image (~25GB)

```bash
## Without the API code (Anonymous mode for local testing)
# docker pull cford38/dolly-v2-3b-azurefunction:latest-anon

## With the API code enabled (for use on Azure Functions on the cloud)
docker pull cford38/dolly-v2-3b-azurefunction:latest
```
_Note: This Docker image will be quite large, so you may need to modify your resource settings in Docker desktop to allow for >5GB of RAM._

## Building and Running the Docker Image Locally
```bash
docker build -t dollyaf .

docker run --gpus all -p 8080:80 --name dollyaf -it dollyaf
```

### Push to DockerHub
```bash
## Without the API code (Anonymous mode for local testing)
# docker tag dollyaf cford38/dolly-v2-3b-azurefunction:latest-anon
# docker push cford38/dolly-v2-3b-azurefunction:latest-anon

## With the API code enabled (for use on Azure Functions on the cloud)
docker tag dollyaf cford38/dolly-v2-3b-azurefunction:latest
docker push cford38/dolly-v2-3b-azurefunction:latest
```

## Create an Azure Function

Here are the example Azure CLI commands for deploying the Docker image-based Function App. Alternatively, you could do similar steps via the Azure Portal at https://portal.azure.com/#create/Microsoft.FunctionApp. 

```bash
az login

## Create Resource Group
az group create --name dolly-dev-rg --location eastus
## Create Storage Account
az storage account create --name dollyst --location eastus --resource-group dolly-dev-rg --sku Standard_LRS

## Create App Service Plan
az functionapp plan create --resource-group dolly-dev-rg --name dolly-asp --location eastus --number-of-workers 1 --sku P3mv3 --is-linux
## Create Function App
az functionapp create --name dolly-func --storage-account dollyst --resource-group dolly-dev-rg --plan dolly-asp --functions-version 4 --os-type Linux --image cford38/dolly-v2-3b-azurefunction:latest
```

That's it! Once the Function app is deployed, you can locate the URL and App key from the service's screen in the Azure Portal.

Please read the accompanying [blog post](https://colbyford.medium.com/deploying-databricks-dolly-on-azure-functions-fac718842d64) for more context into the use of this Docker image.
