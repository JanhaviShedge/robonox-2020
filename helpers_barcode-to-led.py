from pyzbar import pyzbar
import argparse
import cv2

#  Images_list - List of input images, to be gathered from raspberry pi
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

