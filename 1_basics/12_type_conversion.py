x = input("x: ")  # ask for input in terminal
y = x + 1

# input x=1 -> TypeError: can only concatenate str (not "int") to str
# no type conversion (strongly typed language, no implicit conversion)

# Conversions
int(x)  # 1
float(x)  # 1.0
bool(x)  # True
str(x)  # 1

# Falsy values
# ""
# 0
# []
# None (null)
