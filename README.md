# Deploying Databricks Dolly 2.0 on Azure Functions

This repo contains the Docker image and logic for running Databricks Dolyl v2 model on Azure Functions.

## Building and Running the Docker Image Locally
```bash
docker build -t dollyaf .

docker run --gpus all -p 8080:80 --name dollyaf -it dollyaf
```

_Note: This Docker image will be quite large, so you may need to modify your resource settings in Docker desktop to allow for >5GB of RAM._
