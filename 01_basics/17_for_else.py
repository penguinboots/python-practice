names = ["John", "Mary"]

# one way
found = False
for name in names:
    if name.startswith("J"):
        print("Found")
        found = True
        break
if not found:
    print("Not Found")

# better way
for name in names:
    if name.startswith("J"):
        print("Found")
        break
else:
    print("Not found")

# for else loops -> else only performed if loop completed without break statement