#!/usr/bin/python3
import RPi.GPIO as GPIO
from time import sleep

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
	LCDCommand("38")	# Configure Screen
	LCDCommand("01")	# Clear Display
	LCDCommand("0F")	# Display ON and Cursor Blinks
		

def LCDCommand(cmd):
#	print("Command...",cmd)
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
	GPIO.output(2,0)
	GPIO.output(3,0)
	GPIO.output(4,1)
	
	sleep(0.00164)						# Delay
	
	# Set RS, RW, and EN to 1, 0, and 0
	GPIO.output(4,0)
	

def LCDData(data):
#	print("Data...",data)
	# Input should be either a char or a string
	for s in data:						# Separate string into individual chars
		conv = format(ord(s), "x")		# Converts the char into hex
		load(conv)
		
		# Set RS, RW, and EN to 1, 0, and 1
		GPIO.output(2,1)
		GPIO.output(3,0)
		GPIO.output(4,1)
		
		sleep(0.00164)					# Delay
		
		# Set RS, RW, and EN to 1, 0, and 0
		GPIO.output(4,0)

def load(ch):		# Converts the hex input to binary and uploads to pins (D0-D7)
#	print("Loading...", ch)
	binary = bin(int(ch, 16)).zfill(8)	# Convert hex input to binary
	
	c = len(binary)-1
	while binary[c:c+1] != 'b':			# Loop through the number to update each pin
		GPIO.output(len(binary)+4-c, int(binary[c:c+1]))
		c-=1
		
	while c >= 0 and len(binary)+4-c < 13:	# Pads with 0s after the MSB 1
		GPIO.output(len(binary)+4-c, 0)
		c-=1
