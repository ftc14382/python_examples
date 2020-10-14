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
### This example puts some text on the image.
###
font          = cv.FONT_HERSHEY_SIMPLEX
fontScale     = 1
fontThickness = 2
where         = (50, 50) # (pixlels from left, pixels from top)
what          = 'Hello, world!'
#color = (100, 200, 100) # green color in the images color scheme, default BGR
color = (200, 100, 100) # blue color in the images color scheme, default BGR
image_small = cv.putText(image_small, what, where,
                         font, fontScale, color, fontThickness,
                         cv.LINE_AA)
  
cv.imshow("Display window", image_small)
k = cv.waitKey(0)

if k == ord('s'):
    cv.imwrite("skystone_small.png", image_small)
