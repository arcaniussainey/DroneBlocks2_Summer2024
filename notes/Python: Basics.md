# What is Python?
Python is a programming language that is simple, easy to learn, and widely usable in the real world! It's a great language to learn for mathematical processing, computer vision, machine learning, or the quick prototyping of computer software. 

Python is what we would call a high level interpreted language. A **high level language** is one that implements many features or functions for its users, which means less work for us as programmers. An **interpreted language** is one where the source code gets directly executed, and this just means that Python doesn't need compiled. These two things combined mean that Python is simple to write, with tons of features built in, and Python code can be moved between different computers and operating systems without much hassle. 

A Python program file ends in ```.py```, and we execute it by calling the ```python``` executable on it, for example: ```python my_program.py```. If you're using VSCode there will be a run button that does this for you located in the top right. 

When you run a Python program, Python opens the file, goes to the first line of code, and runs the first line. Then, when it finishes, it goes to the next line. We call the line that's currently running the *executing line* and we call the movement of the executing line the *control flow*. The control flow goes from one line to the next by default, but there are ways to move it (which we'll discuss in a bit). 

# Hello World
Let's write our first Python program, Hello World. 

Create a new file with any name you want. I suggest one that's straightforward and simple, such as "hello_world.py". Regardless of what you choose remember to add the ".py" file ending. Once we have that created, let's add the following code:

```Python
print("Hello World") # Outputs the words "Hello World"
```
```text
Hello World
```

Run this program, either by calling Python on the file, or using the button in the top right of VSCode (Requires the Python extension). You should have an output matching the textbox above.

There are two parts of that program I want you to notice. There is ```print("Hello World")``` and ```# Outputs the words "Hello World"```. The section on the left is the actual code, while the section on the right is a comment. Comments in Python start with a ```#``` - and anything following a comment line will be ignored by Python. 

As for the code, we call the ```print``` function (built-in to python) and give it the text ```Hello World``` wrapped in quotation marks. Quotation marks tell Python to treat something as text instead of code. For now, you don't need to fully understand functions or passing stuff to them, just know this is how we can get output. 

# Variables & Types

Let's discuss variables and types in Python, things that will enable us to store data, and understand some of the data we'll be using in our programs. 

### Variables

Variables are storage spots for data. In Python, all (or basically all) types are what we would refer to as Objects, which is something we'll address later. Creating a variable in Python is very simple: we come up with a name Python isn't using, and we use the ```assignment operator``` to give it a value. Our name has to be one word (no spaces), and only use alpha-numeric characters and underscores (A-z, 0-9, and _ ). Variable names are also case-sensitive, so ```my_var``` and ```my_Var``` are two different variables. In Python the assignment operator is the ```=``` character. Here's an example:

```Python
start_text = "Hello World"
```

Because a variable contains a value, we can use it like it *is* that value:

```Python
start_text = "Hello World"
print(start_text)
```
```text
Hello World
```

We can see that this has the same output as not using the variable. It's worth noting that Python will use the value stored in a variable when the line is executed, so if we re-assign a variable before we use it Python won't care about its previous value:

```Python
start_text = "Cooler Hello World~" 
start_text = "Hello World" # We re-assign start_text
print(start_text)
```
```text
Hello World
```

This also applies with the assignment operator. Python won't change the value of a variable until it knows what to change it to, which means we can use a variable in its own assignment operation:

```Python
cool_number = 7

cool_number = cool_number + 3 # Python executes the right half first, "cool_number + 3", and gets 10 as the value
print(cool_number)
```
```text
10
```

This means we can change variables throughout our program, and use the value of our variable to do that. We can use variables as counters, as scores, to hold text, or to save other data. 

### Types
Types are something that variables have, or more specifically, it's what kind of data they are. You've already seen two types: ```int``` and ```string```. An ```int``` or integer, is a number value, like 10. A ```string``` is some text value, like "Hello World". 

Python has a few nice base types:
 - Int = Integer numbers, these are values we can use to hold whole numbers. They can be positive or negative.
 - Float = Decimal numbers, such as 3.1, we can use them to hold fractions or partial values. They are not perfectly exact (try this: ```print(0.1 + 0.1 + 0.1 == 0.3```, "==" checks equality)
 - String = Text data, Python needs to know something is text data. This means you must wrap strings in an indicator character, such as ```"``` or ```'```. It is possible to use the escape character ```\``` before one of those characters to use one of those characters in a string, for example ```print("\"Hello World\"")```.
 - Boolean = True or False, this is pretty simple. We can use the ```not``` keyword to get the opposite value, so ```not True == False``` and ```not False == True```. Any time we use the ```==``` equality operator, the value will be either True or False.

Python also has a few containers, which are types that contain other Objects/variables. We call accessing the values inside of a container "indexing". Here they are:
 - List = A collection of items. We can create a list with square brackets, which can be empty or contain a series of values separated by comments. Ie: ```my_list = []```. We can add and remove items from lists.
 - Tuple = A sequence of items, a Tuple can't be changed after it's made. Tuples are indicated by a set of objects/values separated by commas, contained in parentheses. Ie ```my_tuple = ("hey", "that's", "cool")```
 - Dictionary = A map between names and values. You index a dictionary by using its "key" or the name you gave something in the dictionary. Ie ```my_dictionary = {"keyname": 400}```

Let's look at a quick demo of all of these types being stored in variables and used. 

```Python
cool_string = "Hey, what's up?"
print(cool_string)

silly_float = 7.2452
print(silly_float)

magic_number = 3
print(magic_number)

three_equals_four = (3 == 4)
print("Three Equals Four?")
print(three_equals_four)

number = 11
print(number)

number = number + 5
print(number)

our_list = []
print(our_list)

our_list.append(number) # adds something to list
print(our_list)

our_list.append(silly_float)
our_list.append(cool_string)
our_list.append(magic_number)
print(our_list)

#                 key        value
my_dictionary = {"green": "my favorite", 
                "red": "my least favorite",
                "yellow": "not even a real color"}

print(my_dictionary["green"]) # print the value with the key "green"
# Try other key values!!!!
```

# Operators 
Operators are things which affect other values/variables. We've already used a few, such as the addition operator, assignent operator, and equality operator. The operators we'll discuss here are all binary operators, which means there is one thing on both sides of them. Python will evaluate Operators one at a time, so for example if Python sees ```5 + 10 + 7``` it will calculate ```5 + 10``` into ```15``` and then perform ```15 + 7```. Here are our Operators:

| Operator | Effect | Example |
| -------- | ------ | ------- |
| - | Subtraction | 7 - 5 is 2 |
| + | Addition | 7 + 5 is 12, "box" + "movie" is "boxmovie"|
| * | Multiplication | 4 * 5 is 20, "red" * 5 is "redredredredred"|
| * | Exponentiation ( raise to power) | 2 ** 5 is 32, 4 ** 5 is 1024|
| / | Division | 4 / 5 is 0.8, 5/5 is 1.0|
| // | Floored Division (remove the remainder | 4 // 5 is 0, 5 // 5 is 1 |
| % | Modulus (remainder) | 7 % 5 is 2 |

| Operator | Effect | Example |
| -------- | ------ | ------- |
| == | Equality (check if two values are equal to each other | 3 == 3 is True, True == True is True, 5 == 4 is False |
| <= | Less-Than-Or-Equal ( value on left is less or equal to value on right) | 7 <= 4 is False, 7 <= 7 is True, 7 <= 9 is True |
| >= | Greater-Than-Or-Equal ( value on right is greater or equal to value on right) |7 >= 4 is True, 7 >= 7 is True, 7 >= 9 is False |
| < | Less-Than ( Value on left less than value on right) | 8 < 4 is False, 8 < 8 is False, 8 < 9 is True |
| > | Greater-Than ( Value on left is greater than value on right) | 8 > 4 is True, 8 > 8 is False, 8 > 9 is False |

| Operator | Effect | Example |
| -------- | ------ | ------- |
| = | Assign - changes the value of object on left to value on right | a = 5|
| *= | Multiply and assign | if a is 4 then a *= 5 makes a 20 |
| /= | Divide and assign | if a is 30 then a /= 5 makes a 6.0 |
| %= | Remainder and assign | if a is 10 then a %= 7 makes a 3|
| **= | Exponentiate and assign | if a is 6 then a **= 5 makes a 7776 |
| //= | Floor-divide and assign | if a is 13 then a //= 2 makes a 6|

# Conditionals & Branching
Earlier we mentioned that Python allows us to change the control flow. Now that we know the Operators, one way we can do this is by using Conditionals, things which change the control flow based on the Boolean value of a condition. 

There is one main conditional statement in Python, the ```if``` statement. The ```if``` statement will execute the code contained within its scope if the condition it has is true. *Scope* refers to the area or segment of code that another block of code belongs to. Python uses indentation to indicate scope. Let's look at a very simple if-statement which demonstrates scope. 

```Python
# Main program scope
print("Hi Everyone!")

if True: # if statement, condition is "True"
    # If statement scope, because this indentation follows the if statement and colon
    print("The if-statement ran!")  
    print("This is awesome!!")
```
```text
Hi Everyone!
The if-statement ran!
This is awesome!!
```

Notice how we indented the code following the if-statement. If we indented it without the if-statement, Python would give us an error. But because we have the if-statement, Python knows we're trying to tell it that the code that's indented belongs to the if-statement. The scope of this if-statement will continue until we break the indentation, where the scope will change back to whatever the indentation matches. Let's see an example of this:

```Python
# Main program scope
print("Hi Everyone!")

if True: # if statement, condition is "True"
    # If statement scope, because this indentation follows the if statement and colon
    print("The if-statement ran!")  
    print("This is awesome!!")

# Main program scope
print("We're to the end.")
```
```text
Hi Everyone!
The if-statement ran!
This is awesome!!
We're to the end.
```

What if the if-statement's condition was False? Let's try that.

```Python
# Main program scope
print("Hi Everyone!")

if False: # if statement, condition is "False"
    # If statement scope, because this indentation follows the if statement and colon
    print("The if-statement ran!")  
    print("This is awesome!!")

# Main program scope
print("We're to the end.")
```
```text
Hi Everyone!
We're to the end.
```

Now, the code that's in the scope of the if-statement doesn't run. But our conditional doesn't need to be "True" or "False", it just needs to evaluate (have a value equal to) to True or False. The default value of Python Objects/Variables is True. So this also works:

```Python
# Main program scope
string = "Hello World"

if string: # if statement, condition evaluates to true
    # If statement scope, because this indentation follows the if statement and colon
    print(string)  
    print("This is awesome!!")
```
```text
Hello World
This is awesome!!
```

We can also use our operators to evaluate a condition. This is where the term conditional comes from, like this:

```Python
if False == False: # Our condition is that False is equal to False
    print("That's true!")
```
```text
That's true!
```

We can also use other operators in our conditionals

```Python
if (3 + 5) == 8: # Our condition is that the value on the left (3 + 5) equals the value on the right, 8
    print("3 + 5 is equal to 8!")
```
```text
3 + 5 is equal to 8!
```

Let's consider an example like this: 

```Python
string = "test"

if string == "password": # Our condition is that the variable string equals "password"
    print("You got it right!")
```

If we change ```string``` so this expression evaluates out to true, we'll get our output:

```Python
string = "password"

if string == "password": # Our condition is that the variable string equals "password"
    print("You got it right!")
```
```text
You got it right!
```

But what if we want our program to do something when the condition is false too? This is where the ```else``` keyword comes in. An ```else``` condition only runs when the if-statement above it evaluates to False. Consider this example

string = "test"

if string == "password": # Our condition is that the variable string equals "password"
    print("You got it right!")
else:
    print("You got it wrong... :(")
```
```text
You got it wrong... :(
```

In this case, we get an output either way. Notice that our else-statement is outside the scope of the if-statement, and doesn't have a condition of its own. These are also chained, so if the if-statement evaluates to True the else-statement won't run. Modify the example so the if-statement evaluates to true again! If we wanted to pair another condition with the if statement, we could use the ```elif``` keyword. An ```elif``` has the same rules as an if-statement, but it has to follow after an if-statement, and it won't run if the if-statement is True. 

string = "second_password"

if string == "password": # Our condition is that the variable string equals "password"
    print("You got it right!")
elif string == "second_password":
    print("You found a secret password..")
else:
    print("You got it wrong... :(")
```
```text
You found a secret password..
```

Conditionals are useful when we're wanting to do things in response to user data or sensor input, or when we're calculating things for our programs, or searching for things in lists or files. You'll be able to use them more effectively when you learn more. 

# Loops 
Loops in Python are another way to influence control-flow. Loops repeat code within their scope. How much they repeat this depends on the type of the loop. We have conditional loops, which function similarly to if-statements but repeat the code until the condition stops being true. We also have iteration loops, which loop over variables in a container.

### Conditional Loops
You can create a conditional loop in Python using the ```while``` keyword, which runs code in its scope "while" the condition is true. Consider this for example:

```Python
while True:
    print("Wanna be my friend??")
```

This will loop forever, until we cancel it (which we can do by clicking in the output and typing CTRL+C). We could also use a variable in our loop, and modify it:

```Python
a = 0

while a < 5:
     print("I ran...")
     a = a + 1 # we could also use a += 1
```
```text
I ran...
I ran...
I ran...
I ran...
I ran...
```

Now our loop only plays 5 times. When a loop finishes is lets go of the control flow, and control flow moves to the line after it. 
```Python
a = 0

while a < 5:
     print("I ran...")
     a = a + 1 # we could also use a += 1

print("Loop done?") # Loop exits to here
```
```text
I ran...
I ran...
I ran...
I ran...
I ran...
Loop done?
```

### Iterative Loops
Iterative loops perform a loop over a set of objects or variables. This means they do it once (or more) for every object in a container (though you might skip some objects). We can loop iteratively using the ```for``` keyword. Let's loop over a list:

```Python
our_list = ["Hey", "These", "are", "words", "in", "our", "list"]

for word in our_list: # word will get set equal to every element in "our_list"
    print(word) # print the value stored in list
```
```text
Hey
These
are
words
in
our
list
```

We can also create lists of numbers using the ```range``` function, which accepts a start and end value like this ```range(start, end)``` or a start, end, and skip value like this ```range(start, end, step)```. It will return a list of numbers in the range, moving up by step (default 1) until it reaches the end. See an example:

```Python
for a in range(0, 10):
    print(a)
```
```text
0
1
2
3
4
5
6
7
8
9
```

Or perhaps:

```Python
for a in range(0, 45, 5):
    print(a)
```
```text
0
5
10
15
20
25
30
35
40
```

# Functions & Built-Ins
Functions will be outlined in more depth later, but for now know that they're used to call other pieces of code to do things for us. ```print``` and ```range``` are functions Python provides to us. We will be using many functions provided through DroneBlocks and OpenCV, so it's good to at least understand that they exist. Functions can either accept no input, or can accept input parameters they'll use. ```print``` for instance accepts a string, which it outputs to the terminal, and if you leave it empty it will send an empty message. 

Built-In Functions: 
 - print
 - input
 - str
 - int
 - len
