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
      
cv.imshow("Display window", image_small)
k = cv.waitKey(0)

if k == ord('s'):
    cv.imwrite("skystone_small.png", image_small)
