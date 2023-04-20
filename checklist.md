# Сheck Your Code Against the Following Points

## Don't forget to add `.dockerignore` file before pushing

## Code Style

### 1. Use constants

Good example:
```python
URL = "http://api.weatherapi.com/?"
FILTERING = "Kyiv"

result = requests.get(URL + f"q={FILTERING}")
```

Bad example:
```python   
result = requests.get("http://api.weatherapi.com/?q=Kyiv")
```

### 2. Use uppercase style for constants' names

Good example:
```python
URL = "http://api.weatherapi.com/?"
FILTERING = "Kyiv"
```

Bad example:
```python
url = "http://api.weatherapi.com/?"
filtering = "Kyiv"
```

### 3. The image of the service should be as thin as possible

Good example:
```
FROM python:3.10.8-slim
```

Bad example:
```
FROM python:3.10.8
```
