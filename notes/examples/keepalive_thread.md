# Keepalive Thread
It was outlined prior that to keep our drone active, we should send it a message at least once every ten seconds. While it's possible to do that in our main code, it's easier if we just make a thread dedicated to the task. Consider the following program:

```Python
import threading
import time

thread_active = True

def thread_function(name): # our first function
    while thread_active:
        time.sleep(1)
        print("Thread {0} ran".format(name))

#  ===== Main Loop =====
if __name__ == "__main__":
    print("Main thread started")
    # Create two thread variables with different functions and names
    x = threading.Thread(target=thread_function, args=(1,)) # thread 1
    
    # start both of our threads
    x.start()

    for a in range(0, 5):
        time.sleep(5)
        print("Main thread ran")
    thread_active = False
```

Because we made ```thread_active``` a global variable, it is shared between the scopes of both the if statement and the function```thread_function```. Notice how ```thread_function``` runs in an infinite loop, but still gets interrupted by our main loop code. This is because when we create a thread, Python does the work of figuring out how to switch them out. So, what if we combined something like this with a check on whether or not we had let 10 seconds pass?

```Python
import threading
import time

thread_active = True

def keep_alive(): # our first function
    start_time = time.time()
    while thread_active:
        if (time.time() - start_time) >= 10: # We use greater-or-equal because timing isn't perfectly controlled by us anymore
            print("Ten seconds has passed")
            start_time = time.time()

if __name__ == "__main__":
    print("Main thread started")
    # Create two thread variables with different functions and names
    x = threading.Thread(target=keep_alive, args=()) # thread 1

    x.start() # start our thread

    for a in range(0, 8):
        time.sleep(5)
        print("Main thread ran")
    thread_active = False
```

It looks like this has the effect that we want it to! We can use this as the basis for developing a keep-alive thread, whose only job is to make sure the drone doesn't timeout from inactivity. If we do that we must still remember to add logic for disabling the thread (setting ```thread_active``` to false) if we abort the program/land the drone. 
