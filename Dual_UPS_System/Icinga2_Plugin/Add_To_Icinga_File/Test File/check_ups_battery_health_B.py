#!/usr/bin/python3.6
import os, sys

batteryHealth = 'GOOD(良好)'
if batteryHealth == 'Replace (需更換)':
	print ("Battery Health : "+ batteryHealth + '(Please Change Battery Package !)')
	sys.exit(3)
elif batteryHealth == 'Weak (虛弱)':
	print ("Battery Health : "+ batteryHealth + '(You May Check Battery Package to Change !)')
	sys.exit(3)
else:
	print ("Battery Health : "+ batteryHealth)
	sys.exit(0)
