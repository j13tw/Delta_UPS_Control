#!/usr/bin/python3.6

import os, sys
from decimal import Decimal


outputWatt = '3181'
print ("System output Watt : "+ str(Decimal(outputWatt)/1000) + "KW")
sys.exit(0)
	