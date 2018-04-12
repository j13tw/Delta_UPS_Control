#!/usr/bin/python3.6
import os, sys

batteryStatus = 'OK(良好)'
if batteryStatus == 'Low (低電量)':
	print ("Battery Status : "+ batteryStatus + "(Please Charge battery or Close Service now !)")
	sys.exit(3)
elif batteryStatus == 'Depleted (耗盡)':
	print ("Battery Status : "+ batteryStatus + "(The Battery has no any power !)")
	sys.exit(3)
else:
	print ("Battery Status : "+ batteryStatus)
	sys.exit(0)
	