import os

if os.path.exists("sketch.txt"):
    data = open("sketch.txt")

    for line in data:
        if not line.find(":") == -1:
            (role, line_spoken) = line.split(":", 1)
            print (role, end="")
            print (" said : ", end="")
            print (line_spoken, end="")
    data.close()
else:
    print ("The data file is missing!")
