# Blob Identification
The goal of this activity is to implement a program which allows you to identify a target blob whenever it is within the view of your drone. It should not crash when the blob is outside your drone's view, and it should not identify single pixels as blobs. 

# Project Requirements
 - Display Drone Camera Feed​
 - Accept User Input (Mouse, keyboard, Both, your choice) to control Drone
 - Be able to shutoff/abort drone​ using user input​
 - Implement Blob Detection OR Colored Mass Detection (both is also allowed)

# Example Implementation
This is an example implementation of the project. You are not required to follow this implementation, so long as you manage to complete the activity while meeting all requirements. 

```text
import DroneBlocksTello
import time
import keyboard

define ColorFilter(color, image):
    return CV2 inRange(image, color_min, color_max)

define get_video(drone): # Accept drone in thread
    drone stream_on() # turn on the video
    while program_running:
        set img to dronecamera.frame
        set img_filtered to ColorFilter(img, light_red, dark_red)
        set contours to cv2.findContours(img_filtered, 1, 1) # find the edges of the shape
        set rect to CV2 minAreaRect(contours[0]) # give the smallest rectangle for these contours

        set box to CV2 boxPoints(rect)
        set img to CV2 drawContours(img.copy(), [box], 0, red, 10) # Draw a 10px thick red line around shape

        set area to CV2 contourArea(contours) # find the area of the shape we drew (the rectangle)
        print area # print this to the user

        show_image(img, "Drone Image") # Show the image with the matching title and bounding box

define keep_active(drone):
    while True:
        if program_running is True: # The thread should keep running
            current_time = time.time()
            if (current_time - last_time) > 9:
                # It has been 9 seconds since
                drone send_keepalive()
                set last_time to time.time() 

until an error is encountered:
    # Before Loop
    set tello_drone to DroneBlocksTello()
    set program_running to True
    set last_time to time.time()
    set current_time to time.time() # get the current time

    video = create_thread(target is get_video, args is (tello_drone,))
    drone_alive = create_thread(target is get_video, args is (tello_drone,))

    thread video start() # start this thread
    thread drone_alive start() # start this thread

    tello_drone takeoff()

    while True:  # Enter loop
        set key_input to keyboard read_input()

        if key_input is "w"
            drone go_forward(10)
        else if key_input is "a"
            drone go_left(10in)
        else if key_input is "s"
            drone go_back(10in)
        else if key_input is "d"
            drone go_right(10in)
        else if key_input is "q"
            drone turn_left(30in)
        else if key_input is "e"
            drone turn_right(30in)
        else if key_input is "l"
            drone land(10)
upon error:
    land_drone()
    program_running = False # stop our thread(s)
```

# Helpful Notes
 - Remember how to make variables global on a thread
 - Review your code line by line to catch errors
 - Ensure to have a way to abort your program
 - Remember to have a takeoff feature

# Challenges/Features
 - Improve the readability of the program
 - Improve the program's performance
 - Estimate the distance of a known blob, be able to turn estimation on/off
 - Add the ability to control the move distances
 - Get input in the image screen

# Useful Tutorials:
- Python: Basics
- OpenCV: Basics


# Project Guide

We would suggest that you start from the drone-camera example project. This project makes it easy to work with just the camera features, and allows you to collect any measurements you need, and with threading you'll be able to just turn your code into a function and call it. We can even do that right away

Example:
```Python
from droneblocks.DroneBlocksTello import DroneBlocksTello
import cv2
import numpy as np

me = DroneBlocksTello()
#cap = cv2.VideoCapture(0)
me.connect(True)
print(me.get_battery())
me.streamon()

def camera_function(tello):
  while True:
      img = me.get_frame_read().frame
      #img = cv2.resize(img, (360, 240))
      cv2.imshow("results", img)
      cv2.waitKey(1)

camera_function(me)
```

The next thing to do is to find out where we need to actually focus in this project. The top two segments of the code are just setting up the imports and creating an object. So we want to focus on our function:

```Python
def camera_function(tello):
  while True:
      img = me.get_frame_read().frame
      #img = cv2.resize(img, (360, 240))
      cv2.imshow("results", img)
      cv2.waitKey(1)
```

First, let's find out where we're getting the image. It looks like the line ```img = me.get_frame_read().frame``` is what gathers our image for us. This would replace instances of ```imread```, for example ```im = cv2.imread("blob.jpeg")```. This also means that ```img``` is our image. By default, OpenCV will use BGR (Blue Green Red) color space, which just means the color values for each pixel will be in that order. 

The next line is a comment, but the commented out section would resize our image to be 360x240 pixels. After that, we use ```cv2.imshow``` to show the image with the title "results". And then we wait for a key to be pressed for a single millisecond before restarting the loop. 

With this, we have enough to subsitute any of our example code in. All we need to do is change the name of the image variable to match, and use the image from the camera instead of from a file. For example, our color area calculation example. If we ignore the imports (because we already did them in our new code) then this is all the code:

```Python
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

for contour in contours:
    area = cv2.contourArea(contour) # Get the area of the contours
    print("The area is: " + str(area))

    x,y,w,h = cv2.boundingRect(contour)
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("Image", image) 

# Make python sleep for unlimited time 
cv2.waitKey(0)
```

Remember that we can replace the image line in this code with the one from our drone code. We can also delete or change the code that resizes the image. ```hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)``` just changes the color from BGR to HSV, which means now we use Hue Saturation and Value to determine the color. The "color visualized" example shows us what those colors look like. These lines:

```Python
# Defining lower and upper bound HSV values 
lower = np.array([80, 20, 20])  # HSV - https://www.selecolor.com/en/hsv-color-picker/
upper = np.array([240, 100, 245]) 
```

Allow for us to choose the color range we want to search for, the lowest color, and the highest color. ```mask = cv2.inRange(hsv, lower, upper)``` will set all colors between the lower and upper color to white, and all other colors to black. This is called binary threshholding. After that, we show the two images to the user. This line performs the actual blob detection:

```
contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
```
It finds contours - which are the shapes of the white spots (remember these are the spots where our color was in the image), and it finds the hierarchy of contours - something we'll ignore for our purposes but describes the relationship between the white spots. ```contours``` is a list of all of the white-blobs in our mask (the black and white image). This section:

```
for contour in contours:
    area = cv2.contourArea(contour) # Get the area of the contours
    print("The area is: " + str(area))

    x,y,w,h = cv2.boundingRect(contour)
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
```

Loops over all of the contours using an interative for-loop. Inside that loop we calculate the area of each contour, draw it, create a rectangle around it (```boundingRect```), and then draw that rectangle on our image. The last few lines of the code show the images and wait, which we already have in our code. 

Let's drop this code into our function and see if it works.

```Python
def camera_function(tello):
  while True:
      img = me.get_frame_read().frame
      #img = cv2.resize(img, (360, 240))
        
      # Convert Image to Image HSV 
      hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) 
        
      # Defining lower and upper bound HSV values 
      lower = np.array([80, 20, 20])  # HSV - https://www.selecolor.com/en/hsv-color-picker/
      upper = np.array([240, 100, 245]) 
        
      # Defining mask for detecting color 
      mask = cv2.inRange(hsv, lower, upper) 
      # Display Image and Mask 
      # cv2.imshow("Image", image) # We aren't doing this because we do it later
      cv2.imshow("Mask", mask) 
      
      contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
      
      for contour in contours:
          area = cv2.contourArea(contour) # Get the area of the contours
          print("The area is: " + str(area))
      
          x,y,w,h = cv2.boundingRect(contour)
          cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
      
      cv2.imshow("Image", image) 
      cv2.waitKey(1)
```


And let's drop that function into the rest of our program:

```Python
from droneblocks.DroneBlocksTello import DroneBlocksTello
import cv2
import numpy as np

me = DroneBlocksTello()
#cap = cv2.VideoCapture(0)
me.connect(True)
print(me.get_battery())
me.streamon()

def camera_function(tello):
  while True:
      img = me.get_frame_read().frame
      #img = cv2.resize(img, (360, 240))
        
      # Convert Image to Image HSV 
      hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) 
        
      # Defining lower and upper bound HSV values 
      lower = np.array([80, 20, 20])  # HSV - https://www.selecolor.com/en/hsv-color-picker/
      upper = np.array([240, 100, 245]) 
        
      # Defining mask for detecting color 
      mask = cv2.inRange(hsv, lower, upper) 
      # Display Image and Mask 
      # cv2.imshow("Image", image) # We aren't doing this because we do it later
      cv2.imshow("Mask", mask) 
      
      contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
      
      for contour in contours:
          area = cv2.contourArea(contour) # Get the area of the contours
          print("The area is: " + str(area))
      
          x,y,w,h = cv2.boundingRect(contour)
          cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
      
      cv2.imshow("Image", image) 
      cv2.waitKey(1)

camera_function(me)
```
