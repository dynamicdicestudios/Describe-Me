import cv2
import numpy

# Constants for finding range of skin color in YCrCb
min_YCrCb = numpy.array([80,133,77],numpy.uint8)# may change to [80,133,77]
max_YCrCb = numpy.array([255,173,127],numpy.uint8)

# Grab video frame, decode it and return next video frame
sourceImage = cv2.imread("face.png")

# Convert image to YCrCb
imageYCrCb = cv2.cvtColor(sourceImage,cv2.COLOR_BGR2YCR_CB)

# Find region with skin tone in YCrCb image
skinRegion = cv2.inRange(imageYCrCb,min_YCrCb,max_YCrCb)

# Do contour detection on skin region
contours, hierarchy = cv2.findContours(skinRegion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw the contour on the source image
for i, c in enumerate(contours):
    area = cv2.contourArea(c)
    if area > 1000:
        cv2.drawContours(sourceImage, contours, i, (0, 255, 0), 3)

# Display the source image
cv2.imshow(winname='Skin Colour Detection', mat=sourceImage)

# Wait for a key press to exit
cv2.waitKey(delay=0)

# Close all windows
cv2.destroyAllWindows()
