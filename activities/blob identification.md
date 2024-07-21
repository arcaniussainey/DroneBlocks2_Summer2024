# Remote Controlled Drone
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
