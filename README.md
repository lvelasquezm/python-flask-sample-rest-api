# Python / Flask sample REST API
This is a sample REST API written in [Python](https://www.python.org/)
using [Flask](https://flask.palletsprojects.com/). Available resources are:
* Users.
* Stores.
* Items (within stores).

## Key Features
* RESTful API endpoints.
* Authentication (registration, login, logout).
* JWT integration (access token and refresh token).
* Protected resources/endpoints.

## Development instructions
* Clone this repo:
```shell
$ git clone git@github.com:lvelasquezm/python-flask-sample-rest-api.git
$ cd python-flask-sample-rest-api
```
* Create a python virtual environment and activate it by running (using `python3`):
```shell
$ python3 -m venv venv
$ . venv/bin/activate
```
* Install dependencies (python modules):
```shell
$ pip install -r requirements.txt
```

## Run/Start the API
If you are using [VS Code](https://code.visualstudio.com/) you can run/start the API
within a debugging session by doing the following:
* Install the [Python extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python).
* Make sure to
[select your local python venv](https://code.visualstudio.com/docs/python/python-tutorial#_select-a-python-interpreter)
as your python interpreter in VS Code.
* This repo is already configured with a VS Code python debugging file, so all you will need
to do now is to [start the debugging session](https://code.visualstudio.com/docs/editor/debugging#_run-view).

If you are not using VS Code then just run (within your python venv):
```shell
$ python app.py
```
