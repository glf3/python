import pickle
from athletelist import AthleteList

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        tmp = data.strip().split(",")
        return AthleteList(tmp.pop(0), tmp.pop(0), tmp)
    except IOError as err:
        print ("File Error" + str(err))
        return (None)

def put_to_store(files_list):
    all_athletes = {}
    for filename in files_list:
        tmp = get_coach_data(filename)
        all_athletes[tmp.name] = tmp
    try:
        with open("athletelist.pickle", "wb") as data:
            pickle.dump(all_athletes, data)
    except IOError as err:
        print("File Error(put_to_store)" + str(err))
    return (all_athletes)

def get_from_store():
    all_athletes = {}
    try:
        with open("athletelist.pickle", "rb") as data:
            all_athletes = pickle.load(data)
    except IOError as err:
        print ("File Error(get_from_store)" + str(err))
    return (all_athletes)
print (dir())

the_files = ["sarah2.txt", "james2.txt", "mikey2.txt", "julie2.txt"]
data = put_to_store(the_files)
print (data)

for item in data:
    print (data[item].name + " " + data[item].dob)
