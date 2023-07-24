def multiply(a, b):
    return a * b


# use additional arguments? eg. multiply(2, 3, 4, 5)


def multiplyMore(*list):  # *list is passed as a tuple
    total = 1
    for item in list:
        total *= item
    return total


print(multiplyMore(2, 3, 4, 5))
