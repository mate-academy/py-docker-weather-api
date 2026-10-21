# Docker Weather API

- **Read** [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start
- Look through [Weather API](https://www.weatherapi.com/docs/) documentation, you will need it in this task

## Task

In this task you will be implementing the service for getting current weather
for Paris city. But the most interesting part, that this service must be dockerized
and pushed to the dockerhub. Use [Weather API](https://www.weatherapi.com/docs/) for getting
data about the weather.

The result of this task will be tested by the next commands:
![img.png](result.png)
Of course, instead of `danylott` - it must be your docker id.

So in this task requirements are next:
- The script for getting & printing weather info must be located at `app/main.py`;
- This service must be Dockerized using only `Dockerfile` (`docker-compose.yml` here is forbidden);
- The image of the service should be as thin as possible;
- Use `.dockerignore` file to avoid adding unnecessary stuff to docker image;
- You must use `requests` module for interacting with Weather API;
- You must publish your image to Docker Hub and check it is available for the world;
- You need to generate `API_KEY` for using Weather API, but it shouldn't be hard-coded in `main.py`. 

  You should use environment variables for that purpose. So, read `API_KEY` from environment. 
  And to pass environment variables to docker container use `-e` flag.
- Don't forget to add `.dockerignore` file to your PR;
- You must *modify* this line with correct command to pull your image:
  COMMAND=`docker pull sydneyhart/docker-weather-api:latest`.

<details>
  <summary><strong>Hint</strong></summary>
    Don't use `< >` in docker command. Here is the example:

```docker pull test_user/weather```
</details>

### Note: Check your code using this [checklist](checklist.md) before pushing your solution.

## Run locally

Use Python 3.13 and a key from https://www.weatherapi.com/.
Set `API_KEY` in your environment, then run:

```sh
python -m pip install -r requirements-runtime.txt
python app/main.py
```

The script prints the current Paris weather and exits. Missing credentials,
request failures, and invalid responses produce an error and exit status 1.
The API key is read at runtime; do not commit it or bake it into the image.

## Build and run with Docker

```sh
docker build -t sydneyhart/docker-weather-api:latest .
docker run --rm -e API_KEY sydneyhart/docker-weather-api:latest
```

Only the runtime dependency and application are copied into the slim image.
The container runs as an unprivileged user.

## Publish to Docker Hub

The intended public image is `sydneyhart/docker-weather-api:latest`.
Publication and public pull verification are still pending; the pull command
above becomes usable after these steps complete on a Docker-enabled machine:

```sh
docker login --username sydneyhart
docker buildx build --platform linux/amd64,linux/arm64 \
  -t sydneyhart/docker-weather-api:latest --push .
```

Create or configure `sydneyhart/docker-weather-api` as a public Docker Hub
repository. From a separate, unauthenticated Docker environment, verify:

```sh
docker pull sydneyhart/docker-weather-api:latest
docker run --rm -e API_KEY sydneyhart/docker-weather-api:latest
```

## Tests

```sh
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
flake8 app/
```

Tests mock Weather API responses and require no real API key or network.
