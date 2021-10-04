# Testingmind 2021 - Test Automation Maturity Model

## Description

A simple test automation tool to demonstrate levels of automation maturity.

### The test:
- Starts a chrome browser
- Navigates to a Google URL with a specified search term
- Confirms the browser title includes the search term

### Levels of maturity:

1. Run locally
2. Instructions to run locally on any machine
3. Configure test using parameters
4. Run in a docker container
5. Run automatically in Github Actions

## Prerequisites installed

- Python 3.9
- Chrome
- Chromedriver
- Docker
- Github account

## To use:

### Level 1 & 2:

1. Download repository
2. Enter a terminal window
3. Navigate to the repository root directory
4. Install requirements:  
    `pip install -r requirements.txt`
5. Run test:  
    `pytest -m search_test_v1`

## Level 3:

1. Level 1 & 2 steps
2. (optional) Set or unset environment variables for 1 or more of:
    - BASE_URL : URL to search engine
    - SEARCH_TERMS : Comma separated list of search terms
3. Run test:  
    `pytest -m search_test_v2`

## Level 4:

1. Level 3 steps
2. Build the image from Dockerfile:  
   `docker build -t tm21 .`  
    (on windows, run `build.bat`)
3. Run the docker container (on windows, run `run.bat`):  
    `docker run -e SEARCH_TERMS -e BASE_URL tm21 "-m search_test_v3"`  
    (on windows, run `run.bat`)

## Level 5:

1. Place code in a Github origin repository
2. (optional) Configure `./.github/test_on_push.yml` env parameters
3. Perform a `Push` operation to origin repository
