# The planA project - level 1

## creating a simple microservice that responds to some information

*Always install the latest versions to access all features.

**Installation examples for UBUNTU/Linux system. If necessary, consult the web about your system.

### Requirements

[Docker](https://docs.docker.com/engine/install/ubuntu/) 

[Python 3.8](https://www.python.org/downloads/)

[Pipenv](https://pipenv-es.readthedocs.io/es/stable/)


1. First build the image Docker:

```
$ docker build -t plana .
```

2. Container up with:
```
$ docker run -d -p 5000:5000 --name plana-test plana 
```
3. Testing result in:
```
$ curl -X GET http://%yourip/host%:5000/
```
4. The application returns the JSON response when its /URL path is accessed:

and this respose:
```json
{
  "timestamp": "<current date and time>",
  "hostname": "<Name of the host (IP also accepted)>",
  "engine": "<Name and/or version of the engine running>",
  "visitor ip": "<the IP address of the visitor>"
}
```

5. change image name:
```
$ docker tag plana  %youruser%/plana:latest
```

6. Login in dockerhub
```
$ docker login
```

7. Push the image!
```
$ docker push %youruser%/plana:latest
```

# For Kubernetes

### Requirements

[Kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/)
- access a kubernetes cluster :)

1. apply deployment
```
$ kubectl apply -f deployment.yaml
```

2. apply service
```
$ kubectl apply -f services.yaml
```

3. Get deploy
```
$ kubectl get pods
```