#!/usr/bin/env python

__author__ = "Sai Pc"

netmask  = "255.255.255.192"
gateway = "129.219.234.193"
dns_nameservers = "129.219.17.200"
base_addr_first_three_segs = "129.219.234."
start_ip = 195

# set up for 58 ips in total, mapping
# them to the same nic
for i in xrange(2, 60):
	print "iface eth0:" + str(i) + """ inet static
	address """ + base_addr_first_three_segs + str(start_ip + i) + """
	netmask """ + netmask + """
	gateway """ + gateway + """
	dns-nameservers """ + dns_nameservers
