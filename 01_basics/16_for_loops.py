# python only has 2 types of loops -> for, while

# strings in python are iterable
for x in "Python":
    print(x)

# loop over lists
for x in ["a", "b", "c"]:
    print(x)

# loop over sequence of numbers with built-in range function
for x in range(5):
    print(x)  # prints 0 1 2 3 4
for x in range(2, 5):
    print(x)  # prints 2 3 4
# stepping
for x in range(0, 10, 2):
    print(x) # prints 2 4 6 8

# printing
print(range(5)) # just prints "range(0,5)", a range object
print(type(range(5))) # <class 'range'>  iterable like strings and lists
# range elements take very small amount of memory (eg. range(50000000) is small)
