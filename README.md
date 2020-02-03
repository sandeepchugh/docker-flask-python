# python-docker
python flask app in docker

## Build the image

Now that we have a Dockerfile, let’s verify it builds correctly:
```bash
docker build -t flask-tutorial:latest .
```
After the build completes, we can run the container:
```bash
docker run -d -p 5000:5000 flask-tutorial
```

## Flask Dockerfile

```bash
FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
```

## References

https://runnable.com/docker/python/dockerize-your-flask-application