name = "Sabrina"
print(len(name)) # returns number of items in a container, eg. items in list, chars in string
print(name[0]) # can print char at index in string (S)
print(name[-1]) # can print negative index! (a)
print(name[0:3]) # can slice strings (up to, not including end index)
print(name[:3]) # will pass 0 as starting index
print(name[0:]) # prints entire string
print(name[:]) # prints entire string

# strings are immutable, slices stored in diff memory