import RPi.GPIO as GPIO
import time
from time import sleep

GPIO.setmode(GPIO.BCM)
# For IR sensors
GPIO.setup(3, GPIO.IN)
GPIO.setup(5, GPIO.IN)
GPIO.setup(16, GPIO.IN)

# For bot motors
GPIO.setup(24,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)

# For unloading motor

GPIO.setup(10,GPIO.OUT)
GPIO.setup(9,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)

def readLEDs():
    # This fucntion uses IR sensors to read LEDs and returns the basket number to be carried by the delivery bot
    # If no basket is ready yet, return 0

    led1 = GPIO.input(3)
    led2 = GPIO.input(5)
    led3 = GPIO.input(16)

    if !led1:  # If led1 = 0, then the led at basked 1 is blinking. Similarly for other leds
        return 1
    elif !led2:
        return 2
    elif !led3:
        return 3
    else:
        return 0

def rotatePlatform(degrees):
    # This function rotates the platform by specified number of degrees and sets to delivery bot to a position
    # from where it can move 50 meters forward


    stepsPerRevolution = 60
    numSteps = stepsPerRevolution * (degrees / 360);
    stepper.step(numSteps);

def moveBotForward():
    # This function moves the delivery bot straight by 50 meters

    GPIO.output(24,GPIO.HIGH)
	GPIO.output(23,GPIO.LOW)
	GPIO.output(25,GPIO.HIGH)

    sleep(5) # Time taken to travel 50 meters depending on speed of motor

    #Stop
    GPIO.output(Motor1E,GPIO.LOW)

def moveBotBackward():
    # This function rotates the delivery bot by 180 degrees

    GPIO.output(24,GPIO.LOW)
	GPIO.output(23,GPIO.HIGH)
	GPIO.output(25,GPIO.HIGH)

    sleep(5) # Time taken to travel 50 meters depending on speed of motor

    #Stop
    GPIO.output(Motor1E,GPIO.LOW)

def unloadBot():
    # This function unloads the contents inside the basket, at the cart

    GPIO.output(10,GPIO.HIGH)
	GPIO.output(9,GPIO.LOW)
	GPIO.output(11,GPIO.HIGH)

    sleep(8) # Time taken to unload the Basket

    #Stop
    GPIO.output(Motor1E,GPIO.LOW)

while True:

    basketNo = readLEDs()

    if basketNo == 1:
        degrees = 30
    elif basketNo == 2:
        degrees = 0
    elif basketNo = 3:
        degrees = -30
    else:
        continue

    rotatePlatform(degrees)
    moveBotForward()
    unloadBot()
    moveBotBackward()
    rotatePlatform(-1*(degrees))
