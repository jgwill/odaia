#!/bin/bash
# This script is used to run the app using the virtual environment
#source ./venv/bin/activate
conda activate odaia
python3 run.py "$@"