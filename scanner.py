#!/bin/python3
import sys #allows us to enter CLI arguments etc
import socket #For network activity
from datetime import datetime

#Define our target

#python3 scanner.py <ip address>

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4
else:
	print("invalid Amount of Arguments")
	print("Syntax: python3 scanner.py <ip>")
	sys.exit()
	
#Add a pretty banner
print("."*50)
print("Scanning Target: "+target)
print("Time Started: "+ str(datetime.now()))
print("."*50)
a = input("Starting Port: ")
b = input("Ending Port: ")	
try:
	for port in range(int(a),int(b)):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1) #This is a float
		result = s.connect_ex((target,port)) #Returns error indicator
		print("Checking Port: {}".format(port))
		if result == 0:
			print("Port {} is Open".format(port))
		s.close()
		
		
except KeyboardInterrupt:
	print("\n Exiting Program")
	sys.exit()
	
except socket.gaierror:
	print("Hostname Could Not Be Resovled")
	sys.exit()
	
except socket.error:
	print("Could not connect to the server or IP")
	sys.exit()
		
