# Activity
For your activities we provide two template files under the camp Github page, in the examples folder. There is a threaded template and a normal template. For the RC drone specifically, we’ll be walking you through implementing it.  

We’re attempting to make an RC Drone, that can be controlled while showing its camera view. With that in mind let’s identify the two main features: 
 - Create camera functionality 
 - Create movement functionality 

One of the benefits of working with threads is that we can solve these problems independently, and then combine our solutions later. To do that we just need to turn our code into functions.  

## Getting the Drone Camera 

The  Tello’s camera functionality is relatively easy to access. We have an example on the Github. The code looks something like this:

```Python
from droneblocks.DroneBlocksTello import DroneBlocksTello
import cv2

tello = DroneBlocksTello()
tello.connect(True)
print(tello.get_battery())
tello.streamon()

while True:
    img = tello.get_frame_read().frame
    #img = cv2.resize(img, (360, 240))
    cv2.imshow("results", img)
    cv2.waitKey(1)
```

The actual camera functionality is down at the bottom, this snippet:

```Python
while True:
    img = tello.get_frame_read().frame
    #img = cv2.resize(img, (360, 240))
    cv2.imshow("results", img)
    cv2.waitKey(1)
```

The two things of importance here are the ```tello``` variable, which is a reference to the drone Object, and the ```True``` condition for our while loop. We want to make this a thread, which means we need to change ```True``` to a variable we can set to False. And since we want to make this a function, we need to make sure we make our drone a parameter of the function. Make those changes. 

When you're done, your code should look something like this:

```Python
from droneblocks.DroneBlocksTello import DroneBlocksTello
import cv2

def camera_function(tellodrone):
  while variable_value:
      img = tellodrone.get_frame_read().frame
      #img = cv2.resize(img, (360, 240))
      cv2.imshow("results", img)
      cv2.waitKey(1)
```

We removed the functionality to create the drone for now, as we will do it in the main code where we create our thread. 

## Getting Input & Making Decisions

One way that we can get input is with the ```keyboard``` module's ```read_key``` function. The ```keyboard.read_key()``` function will wait for a user to enter a key, and when they do it will store it in the associated variable. Try this code: (use CTRL+C to exit)

```Python
import keyboard

while True:
    user_in = keyboard.read_key()
    print("Typed: " + user_in)
```

We want to do this to control our code. We can use a combination of if-statements to process the keyboard codes. Consider this example:

```Python
while True:
    k_input = keyboard.read_key()

    if k_input == "w":
        print("Do one thing")
        pass
    elif k_input == "s":
        print("Do a different thing")
        pass
    # Implement other conditions
```

With that, we have some way to control our drone. We can call the drone's different movement functions under different conditions! 

## Combining These

We can take our threaded example program [here](https://github.com/arcaniussainey/DroneBlocks2_Summer2024/blob/main/notes/examples/template%20program%20threaded.md) and modify it. Here it is:

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


We know we want to run our camera function inside the thread, so let's replace the threaded code. We can see that the threaded function has an "insert here" section (and make sure to pass our drone in). Let's do that:

```Python
from droneblocks.DroneBlocksTello import DroneBlocksTello

def threaded_function(tellodrone): # telloReference should be our drone
    while variable_value:
      img = tellodrone.get_frame_read().frame
      #img = cv2.resize(img, (360, 240))
      cv2.imshow("results", img)
      cv2.waitKey(1)

if __name__ == "__main__": # This prevents accidentally starting a thread of the main code
    try:
        tello = DroneBlocksTello()
        tello.connect(True)

        thread = threading.Thread(target=threaded_function, args=(tello,)) # create thread and pass Tello Object
        thread.start()

        # Insert our code here
            
    except Exception: # Something happened, such as a keyboard interrupt or error
        tello.land()
```

After that, we just need to add our main code to the second "insert here" section to get user input working:

```Python
from droneblocks.DroneBlocksTello import DroneBlocksTello

def threaded_function(tellodrone): # telloReference should be our drone
    while variable_value:
      img = tellodrone.get_frame_read().frame
      #img = cv2.resize(img, (360, 240))
      cv2.imshow("results", img)
      cv2.waitKey(1)

if __name__ == "__main__": # This prevents accidentally starting a thread of the main code
    try:
        tello = DroneBlocksTello()
        tello.connect(True)

        thread = threading.Thread(target=threaded_function, args=(tello,)) # create thread and pass Tello Object
        thread.start()

        while True:
            k_input = keyboard.read_key()

            if k_input == "w":
                # Implement forward movement
                pass
            elif k_input == "s":
                # Implement backwards movement
                pass
            # Implement other conditions
            
    except Exception: # Something happened, such as a keyboard interrupt or error
        tello.land()
```

Using this template, you should be able to implement the RC drone!
