#!/usr/bin/python3.6
import os, sys

batteryCharge_Mode = 'Boost Charing(快速充電)'
if batteryCharge_Mode == 'Discharging (未充電)':
	print ("Battery Charge Mode : "+ batteryCharge_Mode + "(Please checked the Power Plug-in !)")
	sys.exit(3)
elif batteryCharge_Mode == 'Resting (休眠)':
	print ("Battery Charge Mode : "+ batteryCharge_Mode + "(Please checked the charge status !)")
	sys.exit(3)
else:
	print ("Battery Charge Mode : "+ batteryCharge_Mode)
	sys.exit(0)
	