name = "Sabrina Wang"

print(name.upper())
print(name.lower())
print(name.title())

name = "  Sabrina Wang"
print(name.strip()) # lstrip or rstrip for removing from one side

print(name.find("Sab")) # returns indexOf or -1, case sensitive
print(name.replace("S", "-"))

print("Sab" in name) # true. can use "not in" for opposite
