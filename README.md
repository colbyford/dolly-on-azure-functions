# Databricks Dolly 2.0 on Azure Functions

## Building the Docker Image
```bash
docker build -t dollyaf .

docker run -p 8080:80 --name dollyaf -it dollyaf
```