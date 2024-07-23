```Python
from droneblocks.DroneBlocksTello import DroneBlocksTello

try:
    tello = DroneBlocksTello()
    tello.connect(True)

    # Insert most of our code here

except Exception: # Something happened, such as a keyboard interrupt or error
    program_active = False # We run this first because tello.land can actually error itself, and we want to ensure our thread ends. 
    #tello.land()
```
