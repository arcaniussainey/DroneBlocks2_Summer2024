### Prerequisites:
 - Python: Basics
 - Psuedocode Intro

# What is a Function?
A function is a block of code we give a name, that only runs when we tell it to, and only has the data we give it. Functions can return data during or at the end of their execution. 

Oftentimes we will write code that is frequently repeated, widly useful, or that we write to help us do something else. Functions allow us to give that code a name, and focus on where or how we use it.

## Functions Intro
A function needs to be defined *somewhere* for us to use it, because the computer needs to know what to do whenever we use it. Some functions, such as ```print``` or ```input``` are given to us by Python. A function will usually consist of a **name**, a set of **parameters** (this can be empty), and some **code**. We decide the **name** of a function, it's **parameters**, and its **code**. 

We refer to defining or creating functions as "declaration". In python functions are *declared* using the ```def``` keyword followed by the name of the function. Once we have the name, we place the set of parameters within a pair of parentheses. Parameters are the names of the variables we want the function to accept. A parameter can only be used within the function it was declared with. After that, any code within the *scope* of the function definition becomes the function's code. Python uses indentation to determine scope. 

We refer to using a function as "calling" it, and we *call* functions by using the function's name followed by the parameters we want to give it enclosed in parentheses. If we have no parameters, the parentheses remain empty. We call filling in a function's parameters "passing" the function values. When a function is called, we leave whatever section of code called it and go to the function's definition. When the function finishes, any data returned gets placed in the spot it was called from. 

## Functions in Python
Here's an example function in Python:

```Python
def my_function():
    print("Isn't this cool?")
```

In this example the function name is ```my_function```, the list of parameters is empty, and the code is a single print statement. Let's call the function and see its output. 

```Python
def my_function():
    print("Isn't this cool?")

my_function() # Function called with no parameters
```
```text
>>> Isn't this cool?
```

Our output was pretty simple. Let's add a parameter:
```Python
def my_function(startmessage):
    print(startmessage)
    print("Isn't this cool?")
```


Now let's call this function and pass it a parameter, then follow what happens. 

```Python
def my_function(startmessage):
    print(startmessage)
    print("Isn't this cool?")

my_function("I can make sandwiches!")
```
```text
>>> I can make sandwiches!
>>> Isn't this cool?
```
Python reads the file from top to bottom. The function definition does get "run", but it doesn't do anything unless we call it so nothing actually happens. On line 5, we call the function. Python goes back to line one, and sets ```startmessage``` to "I can make sandwiches!". Then, it runs the code inside of ```my_function``` - printing ```startmessage``` and printing "Isn't this cool?". 

## Returning from Functions in Python
So we can make a basic function, and throw some code in it, but what if we want to perform some operation that produces data? Like a calculation or checking the status of a device? How would we return this data?

In Python, as most other languages, we use the ```return``` keyword. The ```return``` keyword is provided by python and can only be used within the scope of a Python function. If the Python interpreter ever goes to a line with the return keyword, it will exit the function from that position, and return to where the function was called with whatever value was follows the return function. Let's make a function to multiply a list of numbers, and return the value:

```Python
def multiply_list(our_list):
    value = 1
    for number in our_list:
        value = value * number
    return value
```

Now test this function!

```Python
def multiply_list(our_list):
    value = 1
    for number in our_list:
        value = value * number
    return value

number_list = [4, 5, 2, 6, 4, 5]
multiply_list(number_list)
```

You'll notice that this code doesn't actually give you any result, or print anything out. This is because of how return works. The return value basically substitutes the call to the function, so if we don't do something with that value Python just ignores it the same way it would ignore any other number. Let's print it out:

```Python
def multiply_list(our_list):
    value = 1
    for number in our_list:
        value = value * number
    return value

number_list = [4, 5, 2, 6, 4, 5]
print(multiply_list(number_list)) # This becomes "print(4800)" after the function ends
```
```text
4800
```

Now it's working as we would expect. It's worth noting that you can return from a function at any point, stopping the function from running. For example what if we wanted to create a list of 

## What *are* Functions?
So you know how you can use functions, and how to write them, but what actually *is* a function? A function is actually just the location of its code. When Python, or any other language, sees a function declaration it stores that code separately and waits for us to call it. 

This means that a function's name is actually just a variable with its address. What that means is that if we don't call a function, we can store it in a variable, copy it, or change it. Let's see an example:

```Python
def multiply_list(our_list):
    value = 1
    for number in our_list:
        value = value * number
    return value

number_list = [4, 5, 2, 6, 4, 5]
a = multiply_list # set "a" equal to the address of "multiply_list"

print(a(number_list))
```
```text
4800
```

This is why it's important that we actually call functions, and why we can't just ignore the parentheses if we have no parameters. 

# Using Functions 
When do we use functions? We want to use functions when they make code easier to understand, quicker to write, easier to debug, or allow us to make things more modular. 

For example, we might have some code that looks like this:

```text
set var_a to 10
set var_b to 8
set var_c to square_root(var_a*var_a + var_b*var_b)
```

This is an implementation of the pythagorean theorem. First, notice that there's some functions already present. We didn't write the code for ```square_root```, but we can use it. Now, if we needed to perform this operation a lot, for instance we were calculating a lot of triangles, this code could quickly become messy. For example what if we wanted the perimeter of a triangle, made out of triangles? 

![image](https://github.com/user-attachments/assets/dc865078-7e2a-446e-89a0-abed2f7fa451)

If we wanted to calculate this, we would first need to identify our sides and their lengths, then calculate each side of the red triangle, and then add them. Let's do that.

```text
set var_a to 2.79
set var_b to 4.21
set side_1 to square_root(var_a*var_a + var_b*var_b)

set var_c to 7.78
set var_d to 4.62
set side_2 to square_root(var_c*var_c + var_b*var_d)

set var_e to 1.8
set var_f to 3.14
set side_3 to square_root(var_e*var_e + var_f*var_f)

set perimeter to side_1 + side_2 + side_3
print perimeter
```

Reading this, it's messy. We have repeated the code several times, and every time we do that there's a chance we mess it up. In fact, there's a bug in this example code! Find it by reading the code. Let's replace that with a function and see the difference. 

```text

define pythagorean_theorem(var_1, var_2)
    return square_root(var_1*var_1 + var_2*var_2)

set side_1 to pythagorean_theorem(2.79, 4.21)
set side_2 to pythagorean_theorem(7.78, 4.62)
set side_3 to pythagorean_theorem(1.8, 3.14)

set perimeter to side_1 + side_2 + side_3
print perimeter
```

Now the code is shorter and simpler, and if there *was* an error in the function we would only need to check and fix it in one place.

# Function Summary
So with that we have a very quick introduction to functions in Python! Functions can enable us to have sleek and maintainable code, while reducing errors and writing time. 

## Notes
- Functions only run when called
- Functions allow us to re-use code, reducing errors and making things easier
- Functions can accept and return data
- Functions have a **name**, set of **parameters**, and **code**
- Functions can be passed as variables

## Links
 - https://www.w3schools.com/python/python_functions.asp
 - https://docs.python.org/3.11/tutorial/controlflow.html#defining-functions
