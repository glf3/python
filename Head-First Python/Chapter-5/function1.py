
def sanitize(item):
    if '-' in item:
        spliter = "-"
    elif ':' in item:
            spliter = ":"
    else:
        return item
    (first, second) = item.split(spliter)
    return (first + "." + second)
print (sanitize("2:15"))

with open("james.txt") as James:
    data = James.readline()
james = data.strip().split(",")
print(james)
print(sorted(james))
new_james = sorted([sanitize(item) for item in james])
print(sorted(new_james))

unique_james = []

for item in new_james:
    if item not in unique_james:
        unique_james.append(item)
print(unique_james)

unique_james = set(new_james)
print (unique_james)
print (sorted(unique_james)[0:3])
