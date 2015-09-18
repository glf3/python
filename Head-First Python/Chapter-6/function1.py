def get_coach_data(filename):
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

sarah = get_coach_data("sarah2.txt")
(sarah_name, sarah_dob) = sarah.pop(0), sarah.pop(0)
print (sarah_name + "'s fastest times are : " +
       str(sorted(set([sanitize(t) for t in sarah]))[0:3]))
