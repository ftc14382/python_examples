import cv2 as cv
import sys

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

image_hsv = cv.cvtColor(image_small, cv.COLOR_BGR2HSV)

cv.imshow("Original", image_small)
cv.imshow("Blurred", image_hsv)
k = cv.waitKey(0)

if k == ord('s'):
    cv.imwrite("skystone_small_blurred.png", blur)
