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

new_james = [sanitize(item) for item in james]
new_julie = [sanitize(item) for item in julie]
new_mikey = [sanitize(item) for item in mikey]
new_sarah = [sanitize(item) for item in sarah]
