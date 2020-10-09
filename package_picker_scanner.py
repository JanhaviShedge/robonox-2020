""""Controls module 1 and 3 of the bot 1"""
def getPic():
    """gets the image from camera module"""
    # import the necessary packages
    from picamera.array import PiRGBArray
    from picamera import PiCamera
    import time
    import cv2
    # initialize the camera and grab a reference to the raw camera capture
    camera = PiCamera()
    rawCapture = PiRGBArray(camera)
    # allow the camera to warmup
    time.sleep(0.1)
    # grab an image from the camera
    camera.capture(rawCapture, format="bgr")
    image = rawCapture.array
    return image

def move(x,y,z):
    """moves the suction plate lef, right, up, down, forward, backwards"""
    import RPi.GPIO as GPIO
    from time import sleep

    # Pins for Motor Driver Inputs
    Motor1A = PortNo.
    Motor1B = PortNo.
    Motor1E = PortNo.
    Motor2A = PortNo.
    Motor2B = PortNo.
    Motor2E = PortNo.
    Motor3A = PortNo.
    Motor3B = PortNo.
    Motor3E = PortNo.

    def setup():
    	GPIO.setmode(GPIO.BCM)				# GPIO Numbering
    	GPIO.setup(Motor1A,GPIO.OUT)  # All pins as Outputs
    	GPIO.setup(Motor1B,GPIO.OUT)
    	GPIO.setup(Motor1E,GPIO.OUT)
        GPIO.setup(Motor2A,GPIO.OUT)  # All pins as Outputs
    	GPIO.setup(Motor2B,GPIO.OUT)
    	GPIO.setup(Motor2E,GPIO.OUT)
        GPIO.setup(Motor3A,GPIO.OUT)  # All pins as Outputs
    	GPIO.setup(Motor3B,GPIO.OUT)
    	GPIO.setup(Motor3E,GPIO.OUT)

    def loop(x,y,z):
    	# Going forwards
        if x==1:
        	GPIO.output(Motor1A,GPIO.HIGH)
        	GPIO.output(Motor1B,GPIO.LOW)
        	GPIO.output(Motor1E,GPIO.HIGH)
            sleep(1)
     	# Going backwards
        if x==-1:
        	GPIO.output(Motor1A,GPIO.LOW)
        	GPIO.output(Motor1B,GPIO.HIGH)
        	GPIO.output(Motor1E,GPIO.HIGH)
    	    sleep(1)
    	if y==1:
        	GPIO.output(Motor2A,GPIO.HIGH)
        	GPIO.output(Motor2B,GPIO.LOW)
        	GPIO.output(Motor2E,GPIO.HIGH)
            sleep(1)
    	if y==-1:
        	GPIO.output(Motor2A,GPIO.LOW)
        	GPIO.output(Motor2B,GPIO.HIGH)
        	GPIO.output(Motor2E,GPIO.HIGH)
    	    sleep(1)
        if z==1:
        	GPIO.output(Motor3A,GPIO.HIGH)
        	GPIO.output(Motor3B,GPIO.LOW)
        	GPIO.output(Motor3E,GPIO.HIGH)
            sleep(1)
        if z==-1:
        	GPIO.output(Motor3A,GPIO.LOW)
        	GPIO.output(Motor3B,GPIO.HIGH)
        	GPIO.output(Motor3E,GPIO.HIGH)
    	    sleep(1)

def getboxlocation():
    """Moves the section pump to the middle of the nearest parcel and returns the no of stacks available at the moment."""
    raise NotImplementedError
    import numpy as np
    import imutils
    import cv2
    while True:
        if nearest contour is in middle of the picture or distance==0:
            break
        image = getPic()
        #There's a small assumption that our parcels are all black(which can be changed if needed) while truck's trailer is distinctively different color.
        lower = np.array([0, 0, 0])
        upper = np.array([15, 15, 15])
        shapeMask = cv2.inRange(image, lower, upper)
        #from shapemask, we get the contours using cv2.contours and then find the nearest contour from the middle of picture.
        ncontours= no of contours
        #move towards the nearest contour if any using move function.
    return nContours

def Suction(arg):
    #starts the suction pump if arg=1 and stops if 0.\
    raise NotImplementedError

def zcordinate():
    #returns the z cordinate of suction
    raise NotImplementedError


def distanceFromObject():
    #returns the distance of object that is just down from suction plate
    raise NotImplementedError


def getBin():
    #returns the location of bin that the parcel has to be dropped into in from module 2
    raise NotImplementedError


def droptobin(bin):
    """drops the parcel to the designated bin according to the bin location provided using move() and Suction() functions"""
    raise NotImplementedError


def moveToTruck():
    """Moves the suction plate again inside the truck using moveMethod"""
    raise NotImplementedError

while True:
    nContours=getboxlocation()
    if nContours==0:
        break
    while not distanceFromObject()<0.5:
        move(0,0,-1)
    Suction(1)
    while not zcordinate()>1:
        move(0,0,1)
    while notReachedModule2():
        move(1,0,0)
    while not distanceFromObject()<0.5:
        move(0,0,-1)
    Suction(0)
    bin=getBin()
    droptobin(bin)
    moveToTruck()
