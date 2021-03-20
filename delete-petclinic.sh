#!/bin/sh

# Deploy Petclinic
kubectl delete -f deployment/
kubectl delete -f services/
kubectl delete -f namespace/
