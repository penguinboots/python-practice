def increment(number, by):
    return number + by


# always 2 line breaks after function
print(increment(2, 3))  # prints None without return statement (always returns)


# can return multiple values
def incrementMore(number, by):
    return (number, number + by)


print(incrementMore(2, 3))  # (2, 5) a tuple (read-only list)

# keyword arguments make code more readable
print(incrementMore(2, by=3))  # increment 2 by 3


# assign default values
# by will default to 1 if function called with 1 arg
def incrementDefault(number, by=1):
    return (number, number + by)


# typing parameters and returns
def incrementTypes(number: int, by: int = 1) -> int:
    return number + by
