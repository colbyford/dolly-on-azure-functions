# Deploying Databricks Dolly 2.0 on Azure Functions

This repo contains the Docker image and logic for running Databricks Dolly 2.0 model on Azure Functions.

## Building and Running the Docker Image Locally
```bash
docker build -t dollyaf .

docker run --gpus all -p 8080:80 --name dollyaf -it dollyaf
```

### Push to DockerHub
```bash
docker tag dollyaf cford38/dolly-v2-3b-azurefunction:latest
docker push cford38/dolly-v2-3b-azurefunction:latest
```
_Note: This Docker image will be quite large, so you may need to modify your resource settings in Docker desktop to allow for >5GB of RAM._

## Create an Azure Function

Here are the example Azure CLI commands for deploying the Docker image-based Function App. Alternatively, you could do similar steps via the Azure Portal at https://portal.azure.com/#create/Microsoft.FunctionApp. 

```bash
az login
az group create --name dolly-dev-rg --location eastus
az storage account create --name dollyst --location eastus --resource-group dolly-dev-rg --sku Standard_LRS
az functionapp plan create --resource-group dolly-dev-rg --name dolly-asp --location eastus --number-of-workers 1 --sku P3mv3 --is-linux
az functionapp create --name dolly-func --storage-account dollyst --resource-group dolly-dev-rg --plan dolly-asp --functions-version 4 --os-type Linux --image cford38/dolly-v2-3b-azurefunction:latest
```

That's it! Once the Function app is deployed, you can locate the URL and App key from the service's screen in the Azure Portal.