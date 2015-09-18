from find_it import find_closest
from tm2secs2tm import time2secs, secs2time, format_time

def find_nearest_time(look_for, target_data):
    what = time2secs(look_for)
    time = [time2secs(t) for t in target_data]
    ans = find_closest(what, time)
    return (secs2time(ans))

row_data = {}

with open("PaceData.csv") as paces:
   column_headings = paces.readline().strip().split(",")
   column_headings.pop(0)
   for each_line in paces:
       row = each_line.strip().split(",")
       row_label = row.pop(0)
       inner_dict = {}
       for i in range(len(column_headings)):
           inner_dict[format_time(row[i])] = column_headings[i]

       row_data[row_label] = inner_dict

distance_run = input("Enter the distance attempted: ")
recorded_time = input("Enter the recorded time: ")
predicted_distance = input("Enter the distance you want a prediction for: ")

closest_time = find_nearest_time(format_time(recorded_time), row_data[distance_run])
closest_column_headings = row_data[distance_run][closest_time]

res = [t for t in row_data[predicted_distance].keys()
       if row_data[predicted_distance][t] == closest_column_headings]
print ("The prediction time running " + predicted_distance + " is: "
       + res[0] + ".")




#print (find_nearest_time("59:59", ["56:29", "57:45", "59:03", "1:00:23", "1:01:45"]))
