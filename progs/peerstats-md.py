#!/usr/bin/python

import cjdns
from cjdns import key_utils
import time
import urllib2

nodedb_data_unclean = urllib2.urlopen("https://raw.githubusercontent.com/zielmicha/nodedb/master/nodes")
nodedb_data = nodedb_data_unclean.readlines()
nodedb_data.pop(0)

nodedb_reference_table = {}
for x in nodedb_data:
	nodedb_reference_table[x.split()[0]] = x.split()[1]

cjdns = cjdns.connect("127.0.0.1", 11234, "NONE")

peerStats = cjdns.InterfaceController_peerStats()

list_of_Nodes = []
for x in peerStats['peers']:
	list_of_Nodes.append(key_utils.to_ipv6(x['publicKey']))

Title = "# Virtualhacker - Cjdns public node\n"
date_stamp = "__Last Updated:__ " + time.strftime("%Y-%m-%d, %R")

with open("/var/www/virtualhacker.net/pages/peerstats.md","w") as handle:
	handle.write(Title)
	handle.write(date_stamp + "  \n")
	handle.write("  \n")
	handle.write("To join this Node, information can be found [here](/?pages=services#cjdns)  \n")
	handle.write("  \n")
	handle.write("### Connected Peers  \n")
	handle.write("  \n")
	for x in list_of_Nodes:
		if x in nodedb_reference_table:
			handle.write(x + " - _" + nodedb_reference_table[x] + "_  \n")
		else:
			handle.write(x + "  \n")
