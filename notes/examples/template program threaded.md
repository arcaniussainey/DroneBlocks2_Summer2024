```Python
from droneblocks.DroneBlocksTello import DroneBlocksTello

def threaded_function(TelloReference): # telloReference should be our drone
    pass # insert our code here

if __name__ == "__main__": # This prevents accidentally starting a thread of the main code
    try:
        tello = DroneBlocksTello()
        tello.connect(True)

        thread = threading.Thread(target=threaded_function, args=()) # create thread and pass Tello Object
        thread.start()

        # Insert our code here
            
    except Exception: # Something happened, such as a keyboard interrupt or error
        tello.land()
```
