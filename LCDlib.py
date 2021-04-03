#!/usr/bin/python3
import RPi.GPIO as GPIO
from time import sleep
import datetime

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(2, GPIO.OUT)		# Output pin to RS
GPIO.setup(3, GPIO.OUT)		# Output pin to RW
GPIO.setup(4, GPIO.OUT)		# Output pin to EN

GPIO.setup(5, GPIO.OUT)		# Output pin to D0
GPIO.setup(6, GPIO.OUT)		# Output pin to D1
GPIO.setup(7, GPIO.OUT)		# Output pin to D2
GPIO.setup(8, GPIO.OUT)		# Output pin to D3
GPIO.setup(9, GPIO.OUT)		# Output pin to D4
GPIO.setup(10, GPIO.OUT)	# Output pin to D5
GPIO.setup(11, GPIO.OUT)	# Output pin to D6
GPIO.setup(12, GPIO.OUT)	# Output pin to D7

def LCDInit():
	# Configure Screen
	LCDCommand("38")
	
	# Clear Display
	LCDCommand("01")
	
	# Display ON and Cursor ON
	LCDCommand("0E")
	

def LCDCommand(cmd):
	print("Command...")
	# Load Command into Data Pins
	load(cmd)
	
	# Set RS, RW, and EN to 0, 0, and 1
	GPIO.output(2,0)
	GPIO.output(3,0)
	GPIO.output(4,1)
	
	# Delay
	sleep(0.00164)
	
	# Set RS, RW, and EN to 1, 0, and 0
	GPIO.output(4,0)
	

def LCDData(data):
	print("Data...")
	# Load Character into Data Pins
	print("Data =", data)
	conv = format(ord(data), "x")
	load(conv)
	
	# Set RS, RW, and EN to 1, 0, and 1
	GPIO.output(2,1)
	GPIO.output(3,0)
	GPIO.output(4,1)
	
	# Delay
	sleep(0.00164)
	
	# Set RS, RW, and EN to 1, 0, and 0
	GPIO.output(4,0)

def load(ch):
	print("Loading...")
	# Load D0-D7 with the binary value of 'ch'
	binary = bin(int(ch, 16)).zfill(8)
	
	c = len(binary)-1
	while binary[c:c+1] != 'b':
		print("pin",len(binary)+4-c,"= |",binary[c:c+1],"|")
		GPIO.output(len(binary)+4-c, int(binary[c:c+1]))
		c-=1
		
	while c >= 0 and len(binary)+4-c < 13:
		print("pin",len(binary)+4-c,"= | 0 |")
		GPIO.output(len(binary)+4-c, 0)
		c-=1
	print()

LCDInit()
LCDData('H')
LCDData('e')
LCDData('l')
LCDData('p')

try:
#	while True:
		tFile = open('/sys/class/thermal/thermal_zone0/temp')
		temp = float(tFile.read())
		tFile.close()
		tempC = temp/1000
		tempF = (tempC*1.8)+32
		
		now = datetime.datetime.now()
		
#		print()
#		print("-------------------------------------------")
#		print()
		
		print(now)
		print("  The temperature of the Pi is currently...")
		print("    Celsius = ", tempC)
		print("    Fahrenheit = ", tempF)
		print()
		
#		if tempC > 65:
#			print("  The CPU is HOT")
#			GPIO.output(2,1)
#			GPIO.output(3,0)
#			GPIO.output(4,0)
			
#		elif tempC > 55:
#			print("  The CPU is WARM")
#			GPIO.output(2,1)
#			GPIO.output(3,1)
#			GPIO.output(4,0)
#			
#		elif tempC > 50:
#			print("  The CPU is NORMAL")
#			GPIO.output(2,0)
#			GPIO.output(3,1)
#			GPIO.output(4,0)
#		
#		elif tempC > 45:
#			print("  The CPU is COOL")
#			GPIO.output(2,0)
#			GPIO.output(3,1)
#			GPIO.output(4,1)
#			
#		else:
#			print("  The CPU is COLD")
#			GPIO.output(2,0)
#			GPIO.output(3,0)
#			GPIO.output(4,1)
#		
		sleep(1)
except:
	tFile.close()
	GPIO.cleanup()
	print("Closing Program")
	exit
