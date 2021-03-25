#!/bin/sh

# Deploy Petclinic
kubectl create -f namespace/
kubectl create -f deployment/app-deployment.yaml
kubectl create -f deployment/mariadb-deployment.yaml
kubectl create -f services/app-service.yaml
kubectl create -f services/mariadb-service.yaml


# INSTALL HELM
curl -sSL https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash

# INSTALL Chaos Mesh
kubectl create ns litmus
helm install chaos litmuschaos/litmus --namespace=litmus




# Start and show dashboards for Chaos & Cluster
minikube dashboard &
minikube service -n chaos-testing chaos-dashboard
