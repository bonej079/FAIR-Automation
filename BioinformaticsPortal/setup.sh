#! /bin/bash
# pipenv lock
pipenv --python=$(conda run which python) --site-packages
pipenv install
