#!/usr/bin/python3.6

import os, sys
from decimal import Decimal

outputWatt = outputStatus['outputWatt_A']
print ("System output Watt : "+ str(Decimal(outputWatt)/1000) + "KW")
sys.exit(0)
