#!/bin/sh

# Deploy Petclinic
kubectl create -f namespace/
kubectl create -f deployment/
kubectl create -f services/


# INSTALL HELM
curl -sSL https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash

# INSTALL Chaos Mesh
curl -sSL https://mirrors.chaos-mesh.org/v1.1.2/install.sh | bash


# Start and show dashboards for Chaos & Cluster
minikube dashboard &
minikube service -n chaos-testing chaos-dashboard
