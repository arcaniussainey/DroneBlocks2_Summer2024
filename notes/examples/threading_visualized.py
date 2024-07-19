
## Threading Without Logger
```Python
import threading
import time

def thread_function(name): # our first function
    for i in range(0, 20): # Loop and execute
        time.sleep(1)
        print("Thread: {0} ran".format(name))
    print("Thread: {0} is done".format(name))

def thread_function_2(name): # our second function
    for i in range(0, 10): # loop and execute
        time.sleep(3)
        print("Thread: {0} ran".format(name))
    print("Thread: {0} is done".format(name))


if __name__ == "__main__":
    print("Main thread started")
    # Create two thread variables with different functions and names
    x = threading.Thread(target=thread_function, args=(1,)) # thread 1
    y = threading.Thread(target=thread_function_2, args=(2,)) # thread 2
    
    # start both of our threads
    x.start()
    y.start()
    print("Main thread Done")
```

## Threading With Logger
```Python
import logging
import threading
import time

def thread_function(name): # our first function
    logging.info("Thread %s: starting", name) 
    for i in range(0, 20): # Loop and execute
        time.sleep(1)
        logging.info("Thread %s ran", name)
    logging.info("Thread %s: finishing", name)

def thread_function_2(name): # our second function
    logging.info("Thread %s: starting", name)
    for i in range(0, 10): # loop and execute
        time.sleep(3)
        logging.info("Thread %s ran", name)
    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s" # Create a format for a string formatter. This just tells python where to substitute variables
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S") # Configure the logger to have text

    logging.info("Main    : before creating thread") # Log the thread's start


    # Create two thread variables with different functions and names
    x = threading.Thread(target=thread_function, args=(1,)) # thread 1
    y = threading.Thread(target=thread_function_2, args=(2,)) # thread 2

    logging.info("Main    : before running thread")
    
    # start both of our threads
    x.start()
    y.start()
    logging.info("Main Thread    : all done")
```
