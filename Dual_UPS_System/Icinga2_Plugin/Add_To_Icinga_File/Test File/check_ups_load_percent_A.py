#!/usr/bin/python3.6
import os, sys

outputPercent = '41'
if(int(outputPercent)) <= 75:
	print ("System output Usage Percent : "+ outputPercent + " %| Usage=" + outputPercent + "%;80;90")
	sys.exit(0)
else:
	print ("System output Usage Percent : "+ outputPercent + " % (Load Too Heavy !)" + "| Usage=" + outputPercent + "%;80;90")
	sys.exit(3)
