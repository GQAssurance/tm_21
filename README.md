# Testingmind 2021 - Test Automation Maturity Model

## Description

A simple test automation tool to demonstrate levels of automation maturity.

## Test Steps:
- Starts a chrome browser
- Navigates to a Google URL with a specified search term
- Confirms the browser title includes the search term

## Levels of maturity:

1. Run locally
2. Parameterized tests
3. Containerized testing
4. Run automatically on triggers
5. Run from published test container

# How to use this demo

## Prerequisites needed

Local system needs all of these pre-installed

- Python 3.9
- Chrome
- Chromedriver
- Docker
- Github account

## Level 1:

1. Download repository
2. Enter a terminal window
3. Navigate to the repository root directory
4. Install requirements:  
    `pip install -r requirements.txt`
5. Run test:  
    `pytest -m local`

## Level 2:

1. Level 1 steps
2. (optional) Set or unset environment variables for 1 or more of:
    - BASE_URL : URL to search engine
    - SEARCH_TERMS : Comma separated list of search terms
3. Run test:  
    `pytest -m parameterized`

## Level 3:

1. Level 2 steps
2. Build the image from Dockerfile:  
   `docker build -t tm21 .`
3. Run the docker container:  
    `docker run -e SEARCH_TERMS -e BASE_URL tm21 "-m dockerized"`  

## Level 4:

1. Place code in a Github origin repository
2. (optional) Configure `./.github/test_on_push.yml` env parameters
3. Perform a `Push` operation to origin repository

## Level 5:

1. Level 4 steps
2. Log into Github web interface
3. Select "_Actions_" options
4. Select "_Run tests in published docker image_" workflow
5. Select "_Run workflow_" dropdown
6. (optional) configure the search terms
7. Click "_Run workflow_" button

# Windows convenience batch files

These batch files perform common docker commands for the repo

* build.bat : builds the docker image locally
* run.bat : runs the local docker image
* open.bat : runs the local docker image and enters it in a shell
* pull.bat : pulls the published docker image from Docker hub
