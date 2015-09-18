def get_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        return data.strip().split(",")
    except IOError as error:
        print("File error" + str(error))
        return (None)

def sanitize(item):
    if '-' in item:
        spliter = "-"
    elif ':' in item:
            spliter = ":"
    else:
        return item
    (first, second) = item.split(spliter)
    return (first + "." + second)

james = get_data("sarah.txt")
julie = get_data("james.txt")
mikey = get_data("mikey.txt")
sarah = get_data("sarah.txt")

print ("Pre" + str(james))
print ("Pre" + str(julie))
print ("Pre" + str(mikey))
print ("Pre" + str(sarah))

new_james = sorted([sanitize(item) for item in james])
new_julie = sorted([sanitize(item) for item in julie])
new_mikey = sorted([sanitize(item) for item in mikey])
new_sarah = sorted([sanitize(item) for item in sarah])

print(new_james)
print(new_julie)
print(new_mikey)
print(new_sarah)

print("****************************")
new_james = sorted(set([sanitize(item) for item in james]))
new_julie = sorted(set([sanitize(item) for item in julie]))
new_mikey = sorted(set([sanitize(item) for item in mikey]))
new_sarah = sorted(set([sanitize(item) for item in sarah]))

print(new_james)
print(new_julie)
print(new_mikey)
print(new_sarah)


print("****************************")
print(new_james[0:3])
print(new_julie[0:3])
print(new_mikey[0:3])
print(new_sarah[0:3])
