def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        List = data.strip().split(",")
        dic = {}
        dic["Name"] = List.pop(0)
        dic["Dob"] = List.pop(0)
        dic["Times"] = str(sorted(set(sanitize(t) for t in List))[0:3])
        return dic
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

sarah = get_coach_data("sarah2.txt")
print (sarah["Name"] + "'s fastest time are: " + sarah["Times"])
