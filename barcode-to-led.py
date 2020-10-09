## Code for Pincode (Bar) Detection and LED Output

## Using pyzbar and cv2 libraries for scanning

# Author: Pratiksha Jain

# 1. Get 6 pictures from 6 scanners

# 2. Return pincodes if found from all 6

# 3. Match the best one with pincode

# 4. Give led output

import RPi.GPIO as GPIO
from pyzbar import pyzbar
import argparse
import cv2

# Setting up LEDs # 
GPIO.setmode(GPIO.BCM)
GPIO.setup(30, GPIO.OUT) # red -p1
GPIO.setup(31, GPIO.OUT) # green -p2
GPIO.setup(32, GPIO.OUT) # blue -p3

# Given Barcodes #
given_pincodes = [111111, 111110, 111101]

# 1 #

# Get list from multicam using Arducam Multi Camera Adapter
# And pi camera
# 6 image cameras
# Refer to: 
# https://gist.github.com/skypanther/04b44eaa455f358eb70e59336c068312
Images_list = []



# 2 #

def FindPincode(Images_list, given_pincodes):
	found_pincodes = []

	for image in Images_list:

		detectedBarcodes = pyzbar.decode(image)


		for barcode in detectedBarcodes:

			# We need to convert it to a string first
			barcodeData = barcode.data.decode("utf-8")
			
			# Added the barcode to main list
			found_pincodes.append(barcodeData)

	for pincode in given_pincodes:
		if pincode in found_pincodes:
			return pincode
			break

pincode = FindPincode(Images_list, given_pincodes)

# 3, 4 #

if pincode == given_pincodes[0]:
    GPIO.output(30, True)
    time.sleep(5)
    GPIO.output(30, False)
    
elif pincode == given_pincodes[1]:
    GPIO.output(31, True)
    time.sleep(5)
    GPIO.output(31, False)
else:
    GPIO.output(32, True)
    time.sleep(5)
    GPIO.output(32, False)
