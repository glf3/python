cleese = {}
palin = dict()
print (type(cleese))
print (type(palin))

cleese["Name"] = "John Cleese"
cleese["Occupations"] = ["actor", "comedian", "writer", "film producer"]
palin = {"Name": "Michael Palin", "Occupations": ["comedian", "actor", "writer"]}
print(cleese)
print(palin)


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
sarah_data = {}
sarah_data["Name"] = sarah.pop(0)
sarah_data["Dob"] = sarah.pop(0)
sarah_data["Time"] = sarah

print(sarah_data["Name"] + "'s fastest times are: " +
      str(sorted(set([sanitize(t) for t in sarah_data["Time"]]))[0:3]))
