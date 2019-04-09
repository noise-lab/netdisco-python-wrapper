#!/usr/bin/python3

from netdisco.discovery import NetworkDiscovery
import json

netdis = NetworkDiscovery()

VERSION = 1

print(json.dumps({'version': VERSION}))

netdis.scan()

for dev in netdis.discover():
    print(json.dumps({'device': dev, 'info': netdis.get_info(dev)}))

netdis.stop()
