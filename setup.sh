#!/bin/bash

python=$(which python3)

virtualenv -p $python venv
source venv/bin/activate

pip install -r requirements.txt
