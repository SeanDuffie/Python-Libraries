#!/usr/bin/python3
import RPi.GPIO as GPIO
from time import sleep
import datetime
import LCDlib

LCDlib.LCDInit()

LCDlib.LCDCommand("80")
LCDlib.LCDData("Ce: ")

LCDlib.LCDCommand("C0")
LCDlib.LCDData("Fa: ")

while True:
#	try:
	
		tFile = open('/sys/class/thermal/thermal_zone0/temp')
		temp = float(tFile.read())
		tFile.close()
		tempC = temp/1000
		tempF = (tempC*1.8)+32
		
		now = datetime.datetime.now()

		C = "{:.2f}".format(tempC)
		LCDlib.LCDCommand("8A")
		LCDlib.LCDData(C)
        
		F = "{:.2f}".format(tempF)
		LCDlib.LCDCommand("CA")
		LCDlib.LCDData(F)
		
		print()
		print("-------------------------------------------")
		print()
		
		print(now)
		print("  The temperature of the Pi is currently...")
		print("    Celsius = ", tempC)
		print("    Fahrenheit = ", tempF)
		print()
		
		sleep(1)
		#wait = input("Press Enter to continue.")
		
#	except:
#		tFile.close()
#		GPIO.cleanup()
#		exit()
