# Data Logger Drone
The goal of this activity is to implement a program which logs some data read from your drone to a graph. 

# Project Requirements
 - Display a graph of *some* or *all* sensor data.
 - Be able to shutoff/abort drone​ using user input​

# Example Implementation
This is an example implementation of the project. You are not required to follow this implementation, so long as you manage to complete the activity while meeting all requirements. 

```text
import DroneBlocksTello
import time
import keyboard
import matplotlib.pyplot as plt

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

    drone_alive = create_thread(target is get_video, args is (tello_drone,))

    thread drone_alive start() # start this thread

    tello_drone takeoff()

    set data_points to []

    while True:  # Enter loop
        data_points append (tello_drone getBattery())
        plt plot(data_points)
        plt ylabel('Battery Data Over Time in seconds')
        plt show()
        time.sleep(1)

        set last_time to time.time()
        
upon error:
    land_drone()
    program_running = False # stop our thread(s)
```

# Helpful Notes
 - Remember how to make variables global on a thread
 - Review your code line by line to catch errors
 - Ensure to have a way to abort your program
 - Remember that you can style your graph

# Challenges/Features
 - Improve the readability of the program
 - Improve the program's performance
 - Pair Image-Data with Sensor Data (draw to the image and display, save to a file with metadata, etc.)
 - Add the ability to control the move distances
 - Get input in the image screen

# Useful Tutorials:
 - Python: Basics
 - Matplotlib: Basics
 - Python: Threads
