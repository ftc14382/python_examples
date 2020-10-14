import cv2 as cv
import sys
import numpy as np

img = cv.imread("skystone.png")

if img is None:
      sys.exit("Could not read the image")

(h,w) = img.shape[:2]
if w > 1010:
  ratio = 1020/w
  image_small = cv.resize(img, (int(ratio * w), int(ratio * h)))
else:
  image_small = img

blur = cv.GaussianBlur(image_small, (7,7), 0)

image_hsv = cv.cvtColor(blur, cv.COLOR_BGR2HSV)

lower_yellow = np.array([17, 50, 50])
upper_yellow = np.array([30, 255, 255])

mask_is_yellow  = cv.inRange(image_hsv, lower_yellow, upper_yellow)
mask_not_yellow = cv.bitwise_not(mask_is_yellow)

image_is_yellow_hsv = cv.bitwise_and(image_hsv, image_hsv, mask=mask_is_yellow)
image_is_yellow_rgb = cv.cvtColor(image_is_yellow_hsv, cv.COLOR_HSV2RGB)

cv.imshow("Original", image_small)
cv.imshow("Yellow", mask_is_yellow)
#cv.imshow("Not Yellow", image_not_yellow)
k = cv.waitKey(0)
if k == ord('s'):
    cv.imwrite("skystone_small_blurred.png", blur)
