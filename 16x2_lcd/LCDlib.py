#!/usr/bin/python3
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

RS, RW, EN = 2, 3, 4
GPIO.setup(RS, GPIO.OUT)		# Output pin to RS
GPIO.setup(RW, GPIO.OUT)		# Output pin to RW
GPIO.setup(EN, GPIO.OUT)		# Output pin to EN

D0, D1, D2, D3, D4, D5, D6, D7 = 5, 6, 7, 8, 9, 10, 11, 12
GPIO.setup(D0, GPIO.OUT)	# Output pin to D0
GPIO.setup(D1, GPIO.OUT)	# Output pin to D1
GPIO.setup(D2, GPIO.OUT)	# Output pin to D2
GPIO.setup(D3, GPIO.OUT)	# Output pin to D3
GPIO.setup(D4, GPIO.OUT)	# Output pin to D4
GPIO.setup(D5, GPIO.OUT)	# Output pin to D5
GPIO.setup(D6, GPIO.OUT)	# Output pin to D6
GPIO.setup(D7, GPIO.OUT)	# Output pin to D7

def LCDInit():
	LCDCommand("38")	# Configure Screen
	LCDCommand("01")	# Clear Display
	LCDCommand("0E")	# Display ON and Cursor Blinks
		

def LCDCommand(cmd):
	# 0x01 - Clear Display Screen
	# 0x02 - Return Cursor Home
	# 0x06 - Increment Cursor to right
	# 0x0E - Display ON and Cursor On
	# 0x0F - Display ON and Cursor Blinks
	# 0x80 - Force Cursor to the beginning of the 1st line [replace the second 0 with the desired position in the row]
	# 0xC0 - Force Cursor to the beginning of the 2nd line [replace the second 0 with the desired position in the row]
	# 0x28 - 1 line and 5x7 character matrix (4-bit, D4-D7)
	# 0x38 - 2 lines and 5x7 character matrix (8-bit, D0-D7)
	
	load(cmd)							# Load Command into Data Pins
	
	# Set RS, RW, and EN to 0, 0, and 1
	GPIO.output(RS,0)
	GPIO.output(RW,0)
	GPIO.output(EN,1)
	
	sleep(0.00164)						# Delay
	
	# Set RS, RW, and EN to 1, 0, and 0
	GPIO.output(EN,0)
	

def LCDData(data):
	# Input should be either a char or a string
	for s in data:						# Separate string into individual chars
		conv = format(ord(s), "x")		# Converts the char into hex
		load(conv)
		
		# Set RS, RW, and EN to 1, 0, and 1
		GPIO.output(RS,1)
		GPIO.output(RW,0)
		GPIO.output(EN,1)
		
		sleep(0.00164)					# Delay
		
		# Set RS, RW, and EN to 1, 0, and 0
		GPIO.output(EN,0)

def load(ch):		# Converts the hex input to binary and uploads to pins (D0-D7)
	binary = bin(int(ch, 16)).zfill(8)	# Convert hex input to binary
	
	c = len(binary)-1
	l = D0
	while binary[c:c+1] != 'b':			# Loop through the number to update each pin
		GPIO.output(l, int(binary[c:c+1]))
		l+=1
		c-=1
		
	while c >= 0 and l < D0+8:			# Pads with 0s after the MSB 1
		GPIO.output(l, 0)
		l+=1
		c-=1
