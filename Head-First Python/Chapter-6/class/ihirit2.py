class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times = []):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)
    def top3(self):
        return(sorted(set([sanitize(t) for t in self]))[0:3])


def sanitize(item):
    if '-' in item:
        spliter = "-"
    elif ':' in item:
            spliter = ":"
    else:
        return item
    (first, second) = item.split(spliter)
    return (first + "." + second)

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        tmp = data.strip().split(",")
        return AthleteList(tmp.pop(0), tmp.pop(0), tmp)
    except IOError as err:
        print ("File Error" + str(err))
        return (None)

james = get_coach_data("james2.txt")
julie = get_coach_data("julie2.txt")
mikey = get_coach_data("mikey2.txt")
sarah = get_coach_data("sarah2.txt")

print (james.name + "'s fastest times are: " + str(james.top3()))
print (julie.name + "'s fastest times are: " + str(julie.top3()))
print (mikey.name + "'s fastest times are: " + str(mikey.top3()))
print (sarah.name + "'s fastest times are: " + str(sarah.top3()))
