#!/bin/sh

# Deploy Petclinic
kubectl delete -f deployment/
kubectl delete -f services/
kubectl delete -f namespace/

#Uninstall Chaos-mesh
curl -sSL https://mirrors.chaos-mesh.org/v1.1.2/install.sh | bash -s -- --template | kubectl delete -f -
