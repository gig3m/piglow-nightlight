#!/usr/bin/env python
#####
#
# PyGlow
#
#####
#
# Python module to control Pimoronis PiGlow
# [http://shop.pimoroni.com/products/piglow]
#
# * pulsetest.py - test the pulsing light feature
#
#####


from PyGlow import PyGlow
from time import sleep

pyglow = PyGlow()

times = 999

ramp = range(0,256)

setA = [[1,7,13],[2,8,14],[3,9,15],[4,10,16],[5,11,17]]
setB = [[2,8,14],[3,9,15],[4,10,16],[5,11,17],[1,7,13]]

def opposite(num):
	return (255 - num)

pyglow.all(0)

for n in range(times):
	for i in range(5):
		for brightness in ramp:
			for led in setA[i]:
				pyglow.led(led,opposite(brightness))
			for led in setB[i]:
				pyglow.led(led,brightness)
			if brightness == 255:
				sleep(2)
			sleep(.05)

pyglow.all(0)
# pyglow.led(1)
# pyglow.led(7)
# pyglow.led(13)
