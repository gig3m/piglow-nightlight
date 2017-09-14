#!/usr/bin/env python
#
# Using Piglow to make a fading nightlight
# [http://shop.pimoroni.com/products/piglow]
#
#####


from PyGlow import PyGlow
from time import sleep

pyglow = PyGlow()

# Setup how many iterations we make
# Total runtime will be:
# times * ((ramp length * set length * .05) + 2 )
# 999 * ((255 * 5 * .05) + 2)
# 65,684 seconds = 1094 hours = 45 days
times = 999

# Setup our ramp values
ramp = range(0,256)

# Setup our color sets
# setA fades out
# setB fades in
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
