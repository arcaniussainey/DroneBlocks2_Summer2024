### Prerequisites
 - Python: Basics
 - Python: Functions

# What is a Thread?
A Thread is a second line of execution. We outlined that Python looks at your code line by line, and follows the control-flow. Creating a thread creates a another control-flow, which Python will switch between running. Code running in a thread runs like it's a separate program, but it will share global variables with other threads and with the main program. A thread will also keep access to variables/data that was defined in the scope it was created in. Threads can be created, and the code that created a thread can wait for it to finish. Threads in Python expect to be passed a function to execute alongside the parameters to execute it with. They will run the function until it exits/returns, at which point the thread will die. 

# Using Threads
To create threads we need to use the ```threading``` module. It will provide all the tools necessary to make and manage a thread. 

```Python
import threading
```

Once we've imported threading, creating a thread is pretty simple. We just need a function and some parameters. If our list of parameters is empty we still need to pass an empty tuple, but otherwise there's no special requirements. 

```Python
import threading

def thread_function():
    print("Thread ran")

thread = threading.Thread(target=thread_function, args=())
```

Now once we've created a thread, it doesn't actually *do* anything until we start it. Starting it will run its code. 

```Python
import threading

def thread_function():
    print("Thread ran")

thread = threading.Thread(target=thread_function, args=())
thread.start()
```
```text
Thread ran
```

We can use ```thread.join()``` to wait for a thread to finish execution. Consider these examples with and without the the join. 

```Python
import threading
import time

def thread_function():
    for i in range(0, 5):
        time.sleep(1)
        print("Thread Ran")

thread = threading.Thread(target=thread_function, args=())
thread.start()
print("Main Code Ran")
# thread.join()
print("Main Code Finished")
```
```text
Main Code Ran
Main Code Finished
Thread Ran
Thread Ran
Thread Ran
Thread Ran
Thread Ran
```

Now if we uncomment ```thread.join()```:
```Python
import threading
import time

def thread_function():
    for i in range(0, 5):
        time.sleep(1)
        print("Thread Ran")

thread = threading.Thread(target=thread_function, args=())
thread.start()
print("Main Code Ran")
thread.join()
print("Main Code Finished")
```
```text
Main Code Ran
Thread Ran
Thread Ran
Thread Ran
Thread Ran
Thread Ran
Main Code Finished
```

We can see that our main loop waited at ```thread.join``` until it was over. Remember that ```thread``` is a variable, and so it's only waiting for that specific thread to end. If we wanted to wait for multiple threads to end, we would need multiple join statements. 

We can also do stuff before we wait for a thread to finish. For instance, we might start a separate thread to do a calculation for a variable ```x```, do all the parts of the calculation that don't require x, and then wait for the thread to finish so we can do the remaining calculations. This would be ineffective at speeding the program up, but might let us perform other tasks for the user. 

And remember, we can pass parameters to Threads though we must pass them in a Tuple, and the Tuple most have an open element at the end (meaning it ends in a comma instead of a container element). Consider this example:

```Python
import threading
import time

def thread_function(data):
    for i in range(0, 5):
        time.sleep(1)
        print("Data: " + data)

thread = threading.Thread(target=thread_function, args=("Test",))
thread.start()
print("Main Code Ran")
thread.join()
print("Main Code Finished")
```
```text
Main Code Ran
Data: Test
Data: Test
Data: Test
Data: Test
Data: Test
Main Code Finished
```

Look at this example, and look at the "args" parameter. Its value is ```("Test",)``` rather than ```("Test")```. This is intentional and required for passing parameters to the threading module.

# Thread Locks


# Using Threads
We use threads when we have multiple things we want to do, but don't want to create our own system for switching between tasks. In our case, threads are useful for switching between sending the drone commands and getting the camera feed, for instance. 

Threads will continue to run after your main line of execution is over, so do not create threads you cannot stop/infinite threads without an exit condition. If you do, use the Task Manager on your computer to kill it. Do not command the drone from a thread, always use the main thread for drone commands. 
