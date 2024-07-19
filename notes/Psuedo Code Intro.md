# What is Psuedocode?
Psuedocode: Psuedo- meaning fake, applied to the word code. Just as that name might tell you, psuedocode is fake code, or pretend code, however we still write actual programs. It can't actually be interpreted by the computer, but if it could be, it would actually solve a problem. 

Psuedocode is useful because it can be understood by *humans*. Psuedocode doesn't require any understanding of a programming language to write. It is commonly used to express ideas and algorithms to people regardless of the programming language that they use, if they use any. A mathematician can take an algorithm they've designed to solve a problem and write out a layman's version that anyone could understand - then other mathematicians who can't program can verify it, while programmers can implement it, because they all understand it. 

Psuedocode is also useful because it allows us to express ideas. We can write psuedocode to solve a problem, and then figure out how to actually do it in whatever programming language we want. Likewise, we can find logical flaws in psuedocode by considering what we wrote line by line. 

# Psuedocode Structure
Psuedocode ignores the syntax rules and types of real programming languages. Instead, we try to write it as conveniently as possible. Oftentimes programmers will use psuedocode that reflects languages they have experience with, just as a form of shorthand. In many cases psuedocode will use indentation for scope, and newlines to separate lines of code. Something like this would be psuedocode:

```text
Set Messagetext to "Would you like to cancel?"

Show a messageBox Yes & No Buttons, which displays Messagetext.
Wait for messageBox input, store value in user_input

if user_input equals "Yes":
    Call cancel_subscription()
else:
    Exit
```

It should be somewhat obvious what this program does, despite the fact that you may not know how to display a messagebox or what the ```cancel_subscription``` function does. That is the goal of psuedocode! 

# Good Psuedocode Practices
Good psuedocode should do the following things:
 - Be concise and clear
 - Use non-technical wording when convenient
 - Maintain algorithm details

If psuedocode is too long or complex, it isn't actually helpful to read. If the language is too technical, or the psuedocode is too close to actual programming, then it's not really much easier than actually just writing the program, and it isn't more convenient to think through. On the opposite hand, we don't want to turn an entire algorithm into one line of psuedocode because it doesn't get us any closer to understanding the problem. Psuedocode is about maintaining a balance between being easy to understand and implementation debt (the less detail you put in your psuedocode, the more you have to work when coding it). 

### Bad Psuedocode Examples
