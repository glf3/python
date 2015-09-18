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


vera = AthleteList("vera vi")
vera.append("1.31")
print (vera.top3())
vera.extend(["2.22", "1-21", "2:22"])
print (vera.top3())
