#!/usr/bin/python
#auto-generates ssh config file, using the hostnames and IP addresses found using the DO api
import sys
import requests
import operator
from os import system
import json
from settings import *


droplets = manager.get_all_droplets()
count = 0
f = open('ssh-config.txt', 'w')
while count < len(droplets):
	ip = droplets[count].ip_address.encode("utf-8")
	name = droplets[count].name.encode("utf-8")
	f = open('ssh-config.txt', 'a')
	f.write(config % (name, ip, user, port, interval))
	f.close()
	count = count + 1
f = open('ssh-config.txt', 'a')
f.write(star)
f.close()

