In this python activity, we are going to have the drone autonomously follow an ArUco marker! We have to start by getting our inputs 

```python
from droneblocks.DroneBlocksTello import DroneBlocksTello
import cv2
from cv2 import aruco
import numpy as np
import time
import keyboard
import threading
import math
```

We then need to connect to tello and set up your ArUco detection. You should know how to do this from your other tasks.

Create a Boolean variable "program_running" that the program only runs if it is "True".

Write the main part of the code. The things written in caps lock are for you to complete. Other comments are just there to help you understand.

```python
while program_running:       
    width = 360      # height of screen
    height = 240     # width of screen
    MARKER_ID = 0
    MAX_SPEED = 40
    MIN_DISTANCE = 30

    # SET UP THE CAMERA DISPLAY
    # YOU SHOULD KNOW HOW TO DO THIS FROM OTHER PROJECTS
        
    # USE ARUCO CODE DETECTION TO GET CORNERS AND IDS

    # Look at each ArUco marker to see if it is the one we are looking for
    for index, id in np.ndenumerate(ids):
        # Only run the code if we find the correct ArUco Marker
        if id == MARKER_ID:

            # FIND THE CENTER OF THE ARUCO MARKER
            # THIS IS DONE IN THE "aruco_mouse_tracking.py" IF YOU DO NOT KNOW WHERE TO START
            marker_center_x = # find this
            marker_center_y_ = # find this

            # FIND THE DISTANCE BETWEEN ARUCO CENTER AND CENTER OF THE SCREEN
            dx = # find this
            dy = # find this

            # Use pythagorean theorem to find distance between the ArUco marker and the center of the screen
            distance = math.sqrt((dy**2) + (dx**2))

            # Find the left-right speed needed to fly to the center of the ArUco marker
            l_r_speed = int((MAX_SPEED * dx) / (width // 2))
            # Find the up_down speed needed to fly to the center of the ArUco marker
            u_d_speed = int((MAX_SPEED * dy) / (height // 2) * -1)

            # Check to see how close we are to the center of the ArUco marker
            if abs(distance) <= MIN_DISTANCE:
                print(f"Found Marker {MARKER_ID}!")
            else:
                # Use the .send_rc_control function to move the drone
                tello.send_rc_control(l_r_speed, 0, u_d_speed, 0)

    # Check if key 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
      
    cv2.waitKey(1)

tello.land()
```

