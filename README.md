# The planA project - level 1

## creating a simple microservice that responds to some information

### requirements

- Docker 
- Python 3.8
- Pipenv


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
4. The application should be a web server that returns a JSON response, when its `/` URL path is accessed:

and this respose
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

### requirements

- kubectl
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