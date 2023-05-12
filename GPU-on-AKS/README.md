# GPU-Enabled Azure Function on Azure Kubernetes Service

## Deploy AKS

```bash
az login
az group create --name dolly-dev-rg --location eastus
az aks create --resource-group dolly-dev-rg  --name dolly-aks --node-count 1 --generate-ssh-keys
```

### Update Cluster to user AKS GPU capabilities
From: https://learn.microsoft.com/en-us/azure/aks/gpu-cluster#use-the-aks-specialized-gpu-image-preview

```bash
az extension add --name aks-preview
az extension update --name aks-preview
az feature register --namespace "Microsoft.ContainerService" --name "GPUDedicatedVHDPreview"
az feature show --namespace "Microsoft.ContainerService" --name "GPUDedicatedVHDPreview"
az provider register --namespace Microsoft.ContainerService
```

## Create a Node Pool
```bash
az aks nodepool add --resource-group dolly-dev-rg --cluster-name dolly-aks --name gpunp --node-count 1 --node-vm-size standard_nc24ads_a100_v4 --node-taints sku=gpu:NoSchedule --aks-custom-headers UseGPUDedicatedVHD=true  --enable-cluster-autoscaler --min-count 1 --max-count 1
```

## Deploy and Access Pod
```bash
az aks get-credentials --resource-group dolly-dev-rg --name dolly-aks
kubectl apply -f dolly-gpu-k8s.yaml
kubectl exec -it dolly-gpu-1 -- /bin/bash
```

### Get Service Endpoint
```bash
kubectl get services
```