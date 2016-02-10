#!/usr/bin/env python

__author__ = "Sai Pc"

for i in xrange(2, 60):
	print """iface eth0:""" + str(i) + """ inet static
	address 129.219.234.""" + str(195 + i) + """ 
	netmask 255.255.255.192
	gateway 129.219.234.193
	dns-nameservers 129.219.17.200
"""
