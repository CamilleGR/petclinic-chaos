# Chao à la clinique vétérinaire

Ce dépôt contient un simple déploiement de l'application Petclinic sur Kubernetes. A cela on ajoute du chaos engineering avec Chaos Mesh. Le déploiement n'a été été testé que sur minikube.

## Dockerfile

Le Dockerfile permet de faire créer l'image qui se trouve sur quay.io/camillegr/petclinic. Le Dockerfile se trouve dans le dossier petclinic-container.

## Kubernetes

Dans le namespace Petclinic, on déploie seulement 2 types de ressources pour Petclinic :
* Les deployments qui définissent le déploiement mariadb et le déploiement de petclinic avec 2 replicas.
* Les services Mariadb et l'application Petclinic (Spring-boot).

Chaos-Mesh utilise les CRD pour créer des experimentations.

## Lancer Petclinic et Chaos-Mesh

Pour lancer Petclinic :

`./start-petclinic.sh`

qui va :
- Créer les déploiements/services de petclinic.
- Installer Helm sur minikube.
- Installer Chaos-Mesh.
- Lancer les dahsboards minikube et chaos-mesh.
