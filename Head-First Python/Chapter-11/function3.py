row_data = {}
with open("PaceData.csv") as paces:
    column_headings = paces.readline().strip().split(",")
    column_headings.pop(0)
    for each_line in paces:
        row = each_line.strip().split(",")
        row_label = row.pop(0)
        inner_dict = {}
        for i in range(len(column_headings)):
            inner_dict[row[i]] = column_headings[i]
        row_data[row_label] = inner_dict

times = [t for t in row_data["Marathon"].keys()]
print(times)
times = []
for t in row_data["Marathon"].keys():
    times.append(t)
print(times)
##################

headings = [h for h in sorted(row_data["10mi"].values(), reverse = True)]
print(headings)
headings = []
for h in sorted(row_data["10mi"].values(), reverse = True):
    headings.append(h)
print (headings)
###################

time = [t for t in row_data["20k"].keys() if row_data["20k"][t] == "79.3"]
print(time)
time = []
for t in row_data["20k"].keys():
    if row_data["20k"][t] == "79.3":
        time.append(t)
print(time)
