import cv2 as cv
import sys

img = cv.imread("skystone.png")

if img is None:
      sys.exit("Could not read the image")

cv.imshow("Display window", img)
k = cv.waitKey(0)
