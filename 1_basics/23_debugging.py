def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


# add a breakpoint with F9
print("start")
print(multiply(1, 2, 3))
print("finish")

# F10 to step debugger
# F11 to enter function
