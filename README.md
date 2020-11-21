# Launch Kubernetes Job on-demand using Python

This tutorial is about the Medium article available here: https://medium.com/p/c0efc5ed4ae4

## How to run

To run you will need a Kubernetes engine running (I'm using Minikube).
To launch the entire application you will need to:

- Compile the docker file in app/Dockerfile. Since I'm running minikube I launch it with the contained docker engine `docker build . -t "tutorialk8sjob"`
- Deploy the service account `kubectl apply -f service_account/jobrobot_sa.yaml`
- Deploy the job role `kubectl apply -f service_account/jobrobot_role.yaml`
- Deploy the role binding `kubectl apply -f service_account/jobrobot_rolebinding.yaml`
- Deploy your pod `kubectl apply -f app.yml`

To watch your cluster instantiate pods you want to run `kubectl get pods`. With this you will be able to see the evolving tasks being done and been deleted.

## Requirements

You need to install the package 'kubernetes' on your Python environment. You can do that by running 'pip install kubernetes'.