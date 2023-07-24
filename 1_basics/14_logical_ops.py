# logical and, or, not

name = "Sabrina"

# falsy: 0, "", None, []

if not name:
    print("Name is empty")  # "Sabrina" -> no print, " " -> "Name is empty"

if not name.strip():
    print("Name is empty")  # " " -> no print

age = 22
if age > 18 and age < 65:
    print("Eligible")

# chaining comparison operators
if 18 <= age < 65:
    print("Eligible")
