man = []
other = []

try:
    data = open("sketch.txt")
    for line in data:
        try:
            (role, line_spoken) = line.split(":", 1)
            line_spoken = line_spoken.strip()
            if role == "Man":
                man.append(line_spoken)
            elif role == "Other Man":
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print("datafile is missing!")

print(man)
print(other)

try:
    man_data = open("man.txt", "w")
    other_data = open("other.txt", "w")
    print(man, file=man_data)
    print(other, file=other_data)
    man_data.close()
    other_data.close()
except IOError:
    print("File Error")
