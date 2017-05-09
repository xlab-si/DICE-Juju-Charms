#!/usr/bin/python

import os
import json

ZOOKEEPER_CONFIG = 'zookeeper.json'
NIMBUS_CONFIG = 'nimbus.json'
OUTPUT_CONFIG = 'chef.json'

base_config = {
  "java": {
    "jdk_version": "8",
    "install_flavor": "openjdk"
  },
  "cloudify": {
    "node_id": "juju-storm",
    "deployment_id": "juju-storm-id",
    "properties": {
      #"dns_server": "10.10.43.22",
      "configuration": { }
    },
    "runtime_properties": { }
  }
}
rt_props = base_config['cloudify']['runtime_properties']

def read_json(fname):
    with open(fname) as f:
        conf = json.load(f)
    return conf

is_complete_config = True

if os.path.exists(ZOOKEEPER_CONFIG):
    print "Found Zookeeper configuration"
    zookeeper_conf = read_json(ZOOKEEPER_CONFIG)
    rt_props['zookeeper_quorum'] = [ zookeeper_conf['zookeeper_quorum'] ]
else:
    print "No Zookeeper configuration"
    is_complete_config = False

if os.path.exists(NIMBUS_CONFIG):
    print "Found Nimbus configuration"
    nimbus_conf = read_json(NIMBUS_CONFIG)
    rt_props['storm_nimbus_ip'] = nimbus_conf['storm_nimbus_ip']
else:
    print "No Nimbus configuration"
    is_complete_config = False

with open(OUTPUT_CONFIG, 'w') as f:
    json.dump(base_config, f)
