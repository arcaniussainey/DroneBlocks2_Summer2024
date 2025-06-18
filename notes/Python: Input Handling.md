# What is Input?
Input is the feature of a program to accept data. We often see input in the form of username and password fields, payment details, file uploads, and comment boxes. In our case, input is used to control and orient our drones. 

Python has a built-in function for input, the ```input``` function. The input function accepts a string, which it prints to the terminal, and then waits until a user presses enter. If a user clicks enter/carriage return, then any characters they typed into the terminal get submitted as text input, which the function returns. Try the following program out:

```Python
user_text = input("Try typing something: ") # The input function returns the user's text

print(user_text)
```

It will print out any text the user typed out. Once the user has submitted their input, it is a string we can do whatever we want to. 

# Blocking Vs Non-Blocking User Input 
Blocking input is input that stops the program, or which does something that the program can't move forward without. Non-Blocking input is a form of input that checks if input has been completed, and if not continues the program as usual. There are pros and cons to both approaches. For instance, blocking input can be a bottleneck to a program stopping calculations or preventing simulation. Non-blocking input could result in a program doing something the user didn't want, or it checking too slowly could make input feel unresponsive. We should learn both styles of collecting input in order to choose what benefits us most! 

## Handling Blocking Input
The ```input``` function is a blocking function - when we use it we pause the program. Consider the below example:

```
user_stuff = input("Say Something: ")

print("Notice that this doesn't print until AFTER you input your text.")
```

A blocking input function will block the rest of your program from running until it finishes running (collecting input). In many cases this is perfectly fine, or even preferred, such as collecting user data, or letting a user navigate through a menu or play certain games. For other applications, such as us controlling our drones, this can be problematic. 

One way that we can address this is by using threads. Threads allow us to have a separate context for execution, which means that different code is running at the same time. So we can have a thread which runs code, and then have a program which collects input, or in reverse we could have a thread which runs important code, and a thread which uses input to update what the main code does. Consider the following example:

```Python
import threading

def thread_function(thread_lock):
    while thread_lock.is_set():
        print("How do we do this? ")

if __name__ == "__main__":
    program_active = threading.Event()
    program_active.set() # set a thread lock

    thread = threading.Thread(target=thread_function, args=(program_active,))
    thread.start()
    
    while True:
        user_input = input("Type Text: ")
        if user_input == "end":
            program_active.clear()
            thread.join()
```



## Handling Non-Blocking Input
We could use threads (addressed elsewhere) but it's likely better to use the `keyboard` module. 
# Parsing, Processing, and Input

# Files as User Input

### Parsing Files

### OpenCV File Access
