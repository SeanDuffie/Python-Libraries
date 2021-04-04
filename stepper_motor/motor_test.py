#!/usr/bin/python3
import RPi.GPIO as GPIO
from time import sleep
from datetime import timedelta
import datetime

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

t = .5
step = .002 #.002 is the minimum without slipping
r = 1024 #512 per full rotation

def turn_ccw():
	#print("    Phase 1 = 0001")
	GPIO.output(18, 0)
	GPIO.output(19, 0)
	GPIO.output(20, 0)
	GPIO.output(21, 1)
	sleep(step)
	#print("    Phase 2 = 0010")
	GPIO.output(18, 0)
	GPIO.output(19, 0)
	GPIO.output(20, 1)
	GPIO.output(21, 0)
	sleep(step)
	#print("    Phase 3 = 0100")
	GPIO.output(18, 0)
	GPIO.output(19, 1)
	GPIO.output(20, 0)
	GPIO.output(21, 0)
	sleep(step)
	#print("    Phase 4 = 1000")
	GPIO.output(18, 1)
	GPIO.output(19, 0)
	GPIO.output(20, 0)
	GPIO.output(21, 0)
	sleep(step)

def turn_cw():
	#print("    Phase 1 = 1000")
	GPIO.output(18, 1)
	GPIO.output(19, 0)
	GPIO.output(20, 0)
	GPIO.output(21, 0)
	sleep(step)
	#print("    Phase 2 = 0100")
	GPIO.output(18, 0)
	GPIO.output(19, 1)
	GPIO.output(20, 0)
	GPIO.output(21, 0)
	sleep(step)
	#print("    Phase 3 = 0010")
	GPIO.output(18, 0)
	GPIO.output(19, 0)
	GPIO.output(20, 1)
	GPIO.output(21, 0)
	sleep(step)
	#print("    Phase 4 = 0001")
	GPIO.output(18, 0)
	GPIO.output(19, 0)
	GPIO.output(20, 0)
	GPIO.output(21, 1)
	sleep(step)

try:
	print()
	print("  Initializing...")
	GPIO.output(18, 0)
	GPIO.output(19, 0)
	GPIO.output(20, 0)
	GPIO.output(21, 0)
	print("  Starting Motor...")
	sleep(t)
	
	while True:
		
		print()
		sleep(t/2)
		i = GPIO.input(6)
		if i == 1: break
		print("    Waiting...")
		print()
		sleep(t/2)
		c = 0
		
		print("  Turning Counter-Clockwise...")
		start = datetime.datetime.now()
		while c < r:#i == 0:
			turn_ccw()
			i = GPIO.input(6)
			if i == 1: break
			c += 1
		stop = datetime.datetime.now()
		print("  Completed ", c/512, " turns with a time of ", str(stop-start))
		
		print()
		sleep(t/2)
		i = GPIO.input(6)
		if i == 1: break
		print("  Waiting...")
		print()
		sleep(t/2)
		
		i = GPIO.input(6)
		if i == 1: break
		c = 0
	
		print("  Turning Clockwise")
		start = datetime.datetime.now()
		while c < r:#i == 0:
			turn_cw()
			i = GPIO.input(6)
			if i == 1: break
			c += 1
		stop = datetime.datetime.now()
		print("  Completed ", c/512, " turns with a time of ", str(stop-start))
	
	print()
	print("  Resetting...")
	GPIO.output(18, 0)
	GPIO.output(19, 0)
	GPIO.output(20, 0)
	GPIO.output(21, 0)
	print()
	print("  Program Complete!")		
		
except KeyboardInterrupt:
	GPIO.output(18, 0)
	GPIO.output(19, 0)
	GPIO.output(20, 0)
	GPIO.output(21, 0)
	GPIO.cleanup()
	print()
	print()
	print("Crashed")
