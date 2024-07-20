
This program 
```Python
from droneblocks.DroneBlocksTello import DroneBlocksTello
import cv2
import threading

def read_camera(TelloInstance):
    TelloInstance.streamon()
    while program_active: # While thread is running
        img = TelloInstance.get_frame_read().frame
        img = cv2.resize(img, (360, 240))
        cv2.imshow("results", img)
        cv2.waitKey(1)
    cv2.destroyAllWindows() # close the window
    TelloInstance.streamoff() # disconnect from the Tello camera stream

if __name__ == "__main__": # Ensure this is the file being run
    tello = DroneBlocksTello()
    tello.connect(True)
    
    global program_active # create program_active
    program_active = True
    
    try:
        thread = threading.Thread(target=read_camera, args=(tello,)) # create thread and pass Tello Object
        thread.start()

        while True:
            text = input("Write some text: ")
            print("The user said: " + text)

    except Exception: # Something happened, such as a keyboard interrupt or error
        program_active = False # We run this first because tello.land can actually error itself, and we want to ensure our thread ends. 
        #tello.land()
```
```text
The user said: 
Write some text: Hello World!!!
The user said: Hello World!!!
Write some text: Wowsa!
The user said: Wowsa!
```

You may need to click enter in the terminal to actually refresh it, if you see a bunch of blue and red text about encodings that's likely the case. But after that, a user can interact with the program while it shows the camera feed! Also, the correct way to handle functionality like this is a little harder, but we should technically add logic to break the loop (because of OpenCV) and use a thread lock from the threading module, otherwise our thread may not end. Something similar to this:

```Python
from droneblocks.DroneBlocksTello import DroneBlocksTello
import cv2
import threading
import time


def read_camera(TelloInstance, program_active):
    TelloInstance.streamon()
    time.sleep(1.5) # wait for the drone to process
    while program_active.is_set(): # While thread is running
        img = TelloInstance.get_frame_read().frame
        img = cv2.resize(img, (360, 240))
        cv2.imshow("results", img)
        cv2.waitKey(1)
        if not program_active.is_set():
            break
    cv2.destroyAllWindows() # destroy the OpenCV windows
    TelloInstance.streamoff() # disconnect from the Tello camera stream

if __name__ == "__main__": # Ensure this is the file being run
    tello = DroneBlocksTello()
    tello.connect(True)
    
    try:
        program_active = threading.Event()
        program_active.set() # set a thread lock
        

        thread = threading.Thread(target=read_camera, args=(tello,program_active)) # create thread and pass Tello Object
        thread.start()

        while True:
            text = input("Write some text: ")
            print("The user said: " + text)

    except KeyboardInterrupt: # Something happened, such as a keyboard interrupt or error
        program_active.clear() # This line clears the lock. We run this first because tello.land can actually error itself, and we want to ensure our thread ends.
        print("Waiting to exit")
        thread.join()
```
```text
The user said: 
Write some text: Hello World!!!
The user said: Hello World!!!
Write some text: Wowsa!
The user said: Wowsa!
```
