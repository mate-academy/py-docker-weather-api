<!-- @format -->

## Build Image

docker build --no-cache -t weather-api .

## Run

docker run --env-file .env weather-api
