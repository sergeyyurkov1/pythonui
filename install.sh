#!/bin/bash

sudo apt install python3-venv python3-pip xinit micropolis
python3 -m pip install --upgrade pip

python3 -m venv ~/pythonui/.venv

source .venv/bin/activate
python3 -m pip install -r requirements.txt
