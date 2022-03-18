FROM python:3.8-alpine

RUN apk update
RUN pip install --no-cache-dir pipenv

WORKDIR /usr/src/app

COPY Pipfile Pipfile.lock bootstrap.sh ./
COPY planA-infos ./planA-infos

RUN pipenv install

EXPOSE 5000
ENTRYPOINT ["/usr/src/app/bootstrap.sh"]
