import os

try:
    data = open("sketch.txt")
    for line in data:
        try:
            (role, line_spoken) = line.split(":", 1)
            print(role, end="")
            print(line_spoken, end="")
        except:
            pass
    data.close()
except:
    print("The data file is missing!")
