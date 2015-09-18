import pickle
man = []
other = []
try:
    with open("man.pickle", "wb") as man_file, open("other.pickle", "wb") as other_file:
        pickle.dump(man, man_file)
        pickle.dump(other, other_file)
except pickle.PickleError as perr:
    print("Pickling error:" + str(perr))
