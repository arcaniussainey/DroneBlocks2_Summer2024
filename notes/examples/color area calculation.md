```python
# Importing the libraries OpenCV and numpy 
import cv2 
import numpy as np 
  
# Read the images 
img = cv2.imread("shapes.jpg") # image to use
  
# Resizing the image 
image = cv2.resize(img, (700, 600)) 
  
# Convert Image to Image HSV 
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) 
  
# Defining lower and upper bound HSV values 
lower = np.array([80, 20, 20])  # HSV - https://www.selecolor.com/en/hsv-color-picker/
upper = np.array([240, 100, 245]) 
  
# Defining mask for detecting color 
mask = cv2.inRange(hsv, lower, upper) 
  
# Display Image and Mask 
cv2.imshow("Image", image) 
cv2.imshow("Mask", mask) 

contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


# rea


for contour in contours:
    area = cv2.contourArea(contour) # Get the area of the contours
    print("The area is: " + str(area))

    x,y,w,h = cv2.boundingRect(contour)
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("Image", image) 

# Make python sleep for unlimited time 
cv2.waitKey(0)
```
