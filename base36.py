#!/usr/bin/env python
'''
Script: Base36 Converter
Company: PhishMe, Inc.
Author: R.Tokazowski

Purpose: Base36 math is hard. Here's a script to make it easy. :)
         Targeting CryptoWall malware


'''

import math, sys
base36_abet = "0123456789abcdefghijklmnopqrstuvwxyz"

try:
	value = sys.argv[1]
except:
	print "Usage: python " + sys.argv[0] + " value"

key_length = len(value)-1 # Need to decriment by one to convert correctly

total = 0

for each in value:
	total+= (base36_abet.find(each.lower())+1)*math.pow(36, key_length)
	key_length -=1
print "Base36 conversion: " + str(int(total))