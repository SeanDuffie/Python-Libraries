#!/usr/bin/python3
import RPi.GPIO as GPIO
from time import sleep
import datetime

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)		# Output pin to Red LED
GPIO.setup(3, GPIO.OUT)		# Output pin to Yellow LED
GPIO.setup(4, GPIO.OUT)		# Output pin to Green LED


try:
	while True:
		tFile = open('/sys/class/thermal/thermal_zone0/temp')
		temp = float(tFile.read())
		tFile.close()
		tempC = temp/1000
		tempF = (tempC*1.8)+32
		
		now = datetime.datetime.now()
		
		print()
		print("-------------------------------------------")
		print()
		
		print(now)
		print("  The temperature of the Pi is currently...")
		print("    Celsius = ", tempC)
		print("    Fahrenheit = ", tempF)
		print()
		
		if tempC > 65:
			print("  The CPU is HOT")
			GPIO.output(2,1)
			GPIO.output(3,0)
			GPIO.output(4,0)
			
		elif tempC > 55:
			print("  The CPU is WARM")
			GPIO.output(2,1)
			GPIO.output(3,1)
			GPIO.output(4,0)
			
		elif tempC > 50:
			print("  The CPU is NORMAL")
			GPIO.output(2,0)
			GPIO.output(3,1)
			GPIO.output(4,0)
		
		elif tempC > 45:
			print("  The CPU is COOL")
			GPIO.output(2,0)
			GPIO.output(3,1)
			GPIO.output(4,1)
			
		else:
			print("  The CPU is COLD")
			GPIO.output(2,0)
			GPIO.output(3,0)
			GPIO.output(4,1)
		
		sleep(1)
except:
	tFile.close()
	GPIO.cleanup()
	print("Closing Program")
	exit
