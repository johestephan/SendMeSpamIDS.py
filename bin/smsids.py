import time
import sys
import psutil
import threading
sys.path.append("../lib/")
import server as SC
import responses as RE

services = [["http", 80, RE.DLink_200],
		["TR069", 7547, RE.generic],
		["snmp", 161, RE.generic],
		["IRDMI", 8000, RE.generic],
                ["esmgt", 5601, RE.generic],
                ["FileNail", 4567, RE.generic]]

pidSafe = {}

process = {}


def stop():
	for service in process:
		print "Stopping process %s" % service
		process[service].do_run = False
		process[service].join()
		print process[service].isAlive()

def start():
	du_run = True
	for service in services:
		print "Starting Service  %s ..." % service[0]
		this = threading.Thread(target=SC.run, args=(service[0],service[1],service[2]))
		this.start()
		process.update({service[0]: this})
		


while (True):
	start()
	print str(process)
	print "Kill all processes? (Y/N) "
	keystroke = raw_input()
	if keystroke is "Y" or keystroke is "y":
		stop()
		sys.exit()
