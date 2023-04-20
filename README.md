# Databricks Dolly 2.0 on Azure Functions

## Building the Docker Image
```bash
docker build -t dollyaf .

docker run -p 8080:80 --name dollyaf -it dollyaf
```

_Note: This Docker image will be quite large, so you may need to modigy your resource settings in Docker desktop to allow for >5GB of RAM._
