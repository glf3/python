man = []
other = []
try:
    with open("man.txt", "w") as man_data:
        print(man, file=man_data)
    with open("other.txt", "w") as other_data:
        print(other, file=other_data)
except IOError as err:
    print("File Error" + str(err))
