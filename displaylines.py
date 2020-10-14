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

###
### This example puts two horizontal lines on the image.
###
lineColor     = (200, 100, 100) # blue line in BGR
lineThickness = 2
startX = 0
endX   = 1020
y1     = 250
y2     = 300
cv.line(image_small, (startX, y1), (endX, y1), lineColor, lineThickness)
cv.line(image_small, (startX, y2), (endX, y2), lineColor, lineThickness)

cv.imshow("Display window", image_small)
k = cv.waitKey(0)

if k == ord('s'):
    cv.imwrite("skystone_small.png", image_small)
