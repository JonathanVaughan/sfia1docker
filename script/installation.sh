#!/usr/bin/env bash

sudo apt update -y
 
sudo apt install python3 -y
 
sudo apt install python3-pip -y
 
sudo apt install python3-venv -y
 
python3 -m venv venv
 
cd /var/lib/jenkins/workspace/example_freestyle
 
source /var/lib/jenkins/workspace/example_freestyle/venv/bin/activate
 
pip3 install -r requirements.txt
 
source ~/.bashrc
 
gunicorn --bind=0.0.0.0:5000 app:app

sudo apt update -y

sudo apt install python3 python3-venv python3-pip -y

python3 -m venv