# Dash-MockServer

[![Python CI](https://github.com/ArnaudFlaesch/Dash-MockServer/actions/workflows/ci.yml/badge.svg)](https://github.com/ArnaudFlaesch/Dash-MockServer/actions/workflows/ci.yml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ArnaudFlaesch_Dash-MockServer&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=ArnaudFlaesch_Dash-MockServer)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/a306ad3db39042be81dc772bd5325506)](https://app.codacy.com/gh/ArnaudFlaesch/Dash-MockServer/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
[![Known Vulnerabilities](https://snyk.io/test/github/ArnaudFlaesch/Dash-MockServer/badge.svg)](https://snyk.io/test/github/ArnaudFlaesch/Dash-MockServer)

Flask server returning canned JSON responses for the external APIs used by Dash (OpenWeather, Steam, Strava, Airparif).

## Run locally

```bash
pip install --require-hashes -r requirements-dev.txt
flask --app app run
```

The server listens on `http://localhost:5000`. Requests (GET or POST) whose path contains a fragment listed in `MOCKED_RESPONSES` (`app.py`) get the matching file from `static/`; any other path returns `Not found`.

## Add a mocked endpoint

1. Put the JSON response under `static/<service>/`.
2. Add a `(path fragment, file)` entry to `MOCKED_RESPONSES`, before any entry whose fragment it contains.
3. Add the route to `test_mocked_routes` in `test_app.py`.

## Test

```bash
python -m pytest --cov=app
```

## Update dependencies

Edit `requirements.in` (runtime) or `requirements-dev.in` (tests), then regenerate the hashed lockfiles:

```bash
pip-compile --generate-hashes --allow-unsafe --strip-extras --no-emit-index-url -o requirements.txt requirements.in
pip-compile --generate-hashes --allow-unsafe --strip-extras --no-emit-index-url -o requirements-dev.txt requirements-dev.in
```

## Docker

```bash
docker build -t dash-mockserver .
docker run -p 5000:5000 dash-mockserver
```
