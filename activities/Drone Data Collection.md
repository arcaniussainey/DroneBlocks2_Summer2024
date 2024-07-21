# Remote Controlled Drone
The goal of this activity is to implement a program which allows you to collect data in the field using your drone.

# Project Requirements
 - Save Images from Drone Camera Feed
 - Accept User Input (Mouse, keyboard, Target, Both, your choice) to control Drone
 - Be able to shutoff/abort drone​ using user input​

# Example Implementation
This is an example implementation of the project. You are not required to follow this implementation, so long as you manage to complete the activity while meeting all requirements. 

```text
import DroneBlocksTello
import time
import keyboard

define take_photo():
    set img to dronecamera.frame
    return image

define save_photo(photo):
    save photo to filesystem

define get_video(drone): # Accept drone in thread
    drone stream_on() # turn on the video
    while program_running:
        set img to dronecamera.frame
        show_image(img, "Drone Image") # Show the image with the matching title

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
        else if key_input is "p"
            set picture to take_photo()
            save_photo(picture)

upon error:
    land_drone()
    program_running = False # stop our thread(s)
```

# Helpful Notes
 - Remember how to make variables global on a thread
 - Review your code line by line to catch errors
 - Ensure to have a way to abort your program
 - Remember that movement can add blur/noise to your photos

# Challenges/Features
 - Have your drone take pictures of specific targets/things you need data on automatically (not too many though, maybe a timer between auto-photos)
 - Automatically label/organize your collected data. Perhaps this means the user can change what folder data gets saved to with their input.
 - Take and average multiple photos to remove noise before saving the pictures

# Useful Tutorials:
- Python: Basics
- Python: Threading
- OpenCV: Basics
