# What is Input?
Input is the feature of a program to accept data. We often see input in the form of username and password fields, payment details, file uploads, and comment boxes. In our case, input is used to control and orient our drones. 

### Input with `input`
Python has a built-in function for input, the ```input``` function. The input function accepts a string, which it prints to the terminal, and then waits until a user presses enter. If a user clicks enter/carriage return, then any characters they typed into the terminal get submitted as text input, which the function returns as a string. Try the following program out:

```Python
user_text = input("Try typing something: ") # The input function returns the user's text

print(user_text)
```

It will print out any text the user typed out. Once the user has submitted their input, it is a string we can do whatever we want to. 

### Input with Keyboard
The `keyboard` module handles input differently. It registers with the operating system, watched for 'events' - specific actions it should respond to. This basically means we can listen for individual keys. 

We must install the `keyboard` module, which is simple enough! Using the CMD, we can run `pip install keyboard`. That should download the module we need. 

Once we've downloaded it, we need to remember to import the module:

```python
import keyboard
```

Now, we're setup to use it! The keyboard module allows a few cool things:
 - Waiting - Keyboard can wait for a specific key to be pressed, and will stop the program until this happens (called blocking)
 - Adding Hotkeys - Hotkeys are keys that cause a certain behavior or event. For instance ALT+TAB, CTRL+ESC, or CTRL+C/CTRL+V are all some example hotkeys!
 - Hooking Keys - This is like adding hotkeys, but for specific individual keys.

#### Waiting for keys
This allows us to wait for either a specific key, or any key. 

**Specific Key**
To wait for a specific key we can use `keyboard.wait`, as below:

```python
import keyboard

keyboard.wait('esc')
print("User clicked escape")

keyboard.wait('esc+a')
print("User clicked escape plus A")
```

Notice that it doesn't just accept a single key, but a `parseablehotkey`. This means you can specify multiple characters. 

**Awaiting any key**
We can also wait for a key to be pressed in general, and then use it. We do this using `keyboard.read_key`. This function will return a `Key_` type, so if we're checking for specific keys we want to convert it to a string first. 

```python
while True:
    key_pressed = str(keyboard.read_key()) # The str method converts to a string

    if key == "a":
        print("Lowercase a")
    elif key == "A":
        print("Uppercase A")
    else:
        print("Something else...")
```
If we want to listen without paying attention to capitalization, we can lowercase the string
```python
while True:
    key_pressed = str(keyboard.read_key()).lower() # The str method converts to a string

    if key == "a":
        print("Lowercase OR Uppercase a")
    else:
        print("Something else...")
```


#### Adding Hotkeys
```python
import keyboard


keyboard.add_hotkey('ctrl+shift+a', print, args=('triggered', 'hotkey'))
```

The method expects the following parameters:
```
hotkey: _ParseableHotkey,
callback: (...) -> (bool | None),
args: _Ts = (),
suppress: bool = False,
timeout: float = 1,
trigger_on_release: bool = False
```

Either provided in that order, or with the specific varnames specified. I will explain each parameter below:
 - Hotkey - This is what the user should actually click (together) specified as a string. Ie, 'ctrl+h'
 - Callback - A callback is a function that should be 'called' (or run) when some behavior happens. In our example above, that's the print method.
 - Args - This is a tuple (value specified in parenthesis, it cannot be modified) that gets passed to the function specified in `callback`. In our example it is ('triggered', 'hotkey'). When combined with the callback `print`, it becomes `print('triggered', 'hotkey')`.
 - Suppress - Optional, defaults to False. This is whether to 'suppress' the keys, meaning that they won't go through to the target program. Only use this if you want to prevent keys from messing with the user's app.
 - Timeout - Optional, defaults to 1. This is how long the user has in seconds to click all keys together. 
 - Trigger on release - Optional, defaults to false. This determines whether a hotkey triggers when the user first presses it down, or only when they release all keys.



#### Hooking Keys



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
### Using Threads

### Using Keyboard
# Parsing, Processing, and Input

# Files as User Input

### Parsing Files

### OpenCV File Access
