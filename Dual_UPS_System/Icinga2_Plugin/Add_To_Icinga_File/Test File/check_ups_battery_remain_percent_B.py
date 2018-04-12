#!/usr/bin/python3.6
import os, sys

batteryRemain_Percent = '100'
if(int(batteryRemain_Percent)) >= 30:
	print ("Battery Remain Percent : "+ batteryRemain_Percent + " %| Battery Level=" + batteryRemain_Percent + "%;50;30")
	sys.exit(0)
else:
	print ("Battery Remain Percent : "+ batteryRemain_Percent + " % (Quick Close All Service !)" + "| Battery Level=" + batteryRemain_Percent + "%;50;30")
	sys.exit(3)
	