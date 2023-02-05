#!/bin/bash

if [ ! -d "~/.env" ] 
then
  python -m venv .env
  echo "venv already exists"
fi
source .env/bin/activate
python -m pip install -r requirements.txt
