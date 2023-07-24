# local variables
# python has no block level scope
# defining variable inside block -> still accessible outside of block (eg. inside a for loop -> outside of the for loop, inside same function)

# global variables
# accessible in any function

message = "a"


def greet():
    message = "b"


greet()
print(message)  # still prints 'a'

# message became a new local variable within the greet function


# modifying global inside function (don't do this!!)
def greet2():
    global message
    message = "b"

greet2()
print(message)
