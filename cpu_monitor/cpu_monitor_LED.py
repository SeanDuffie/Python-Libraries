#!/usr/bin/python3
import RPi.GPIO as GPIO
from gpiozero import LED
from time import sleep
import datetime

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)

while True:
    try:
        tFile = open('/sys/class/thermal/thermal_zone0/temp')
        
        temp = float(tFile.read())
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
            GPIO.output(17,1)
            print("  The CPU is HOT")
            GPIO.output(2,1)
            GPIO.output(3,0)
            GPIO.output(4,0)
            
        elif tempC > 55:
        	GPIO.output(17,1)
        	print("  The CPU is WARM")
        	GPIO.output(2,1)
        	GPIO.output(3,1)
        	GPIO.output(4,0)
        	
        elif tempC > 50:
        	GPIO.output(17,1)
        	print("  The CPU is NORMAL")
        	GPIO.output(2,0)
        	GPIO.output(3,1)
        	GPIO.output(4,0)
        
        elif tempC > 45:
        	GPIO.output(17,1)
        	print("  The CPU is COOL")
        	GPIO.output(2,0)
        	GPIO.output(3,1)
        	GPIO.output(4,1)
        	
        else:
            GPIO.output(17,0)
            print("  The CPU is COLD")
            GPIO.output(2,0)
            GPIO.output(3,0)
            GPIO.output(4,1)
        
        sleep(1)
        # wait = input("Press Enter to continue.")
        
    except:
        print("Closing Program...")
        tFile.close()
        GPIO.cleanup()
        exit
