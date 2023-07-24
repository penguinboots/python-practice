x = 1  # x -> label for memory location for 1
print(id(x))  # prints "4385970808", address for memory location

x = x + 1 # re-rereference
print(id(x)) # prints "4354710168" -> new address because ints are immutable
# unreferenced memory 4385970808 will be released at some point by python gargabe collector

# set x to mutable type
x = [1, 2, 3]
print(id(x)) # 4366226624

x.append(4)
print(id(x)) # 4366226624
# lists are mutable -> changes applied at same memory location