from netdisco.discovery import NetworkDiscovery
import json

netdis = NetworkDiscovery()

netdis.scan()

for dev in netdis.discover():
    print(json.dumps({'device': dev, 'info': netdis.get_info(dev)}))

netdis.stop()
