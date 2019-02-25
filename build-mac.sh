#!/bin/bash

git clone https://github.com/home-assistant/netdisco.git
mv netdisco netdisco.git
mv netdisco.git/netdisco .
rm -rf netdisco.git

python3 -m virtualenv env
source env/bin/activate

pip install requests
pip install zeroconf
pip install typing

python -m PyInstaller --onefile device_identifier_mac.spec



