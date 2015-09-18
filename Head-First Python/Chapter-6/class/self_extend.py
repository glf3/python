class Athlete:
    def __init__(self, a_name, a_dob = None, a_times = []):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times
    def top3(self):
         return (sorted(set([sanitize(t) for t in self.times]))[0:3])
    def add_time(self, value):
        self.times.append(value)
    def add_times(self, list_value):
        self.times.extend(list_value)

#########################################
def sanitize(string):
    spliter = "."
    if ":" in string:
        spliter = ":"
    elif "-" in string:
        spliter = "-"
    else:
        return string
    (first, second) = string.split(spliter)
    return str(first+"."+second)

def get_coach_data(filename):
     try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(",")
        return Athlete(templ.pop(0), templ.pop(0), templ)
     except IOError as err:
        print ("File Error" + str(err))
        return (None)

########################################
    
james = get_coach_data("james2.txt")
julie = get_coach_data("julie2.txt")
mikey = get_coach_data("mikey2.txt")
sarah = get_coach_data("sarah2.txt")

print (james.name + " 's fastest times are: " + str(james.top3()))
print (julie.name + " 's fastest times are: " + str(julie.top3()))
print (mikey.name + " 's fastest times are: " + str(mikey.top3()))
print (sarah.name + " 's fastest times are: " + str(sarah.top3()))

vera = Athlete("Vera Vi")
vera.add_time("1.31")
print (vera.top3())
vera.add_times(["2.22", "1-21", "2:22"])
print (vera.top3())
