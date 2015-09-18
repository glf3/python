from math import *
def find_closest(look_for, target_data):

    def diff_(first, second):
        return abs(first-second)

    max_diff = 9999999
    for each_thing in target_data:
        diff = diff_(each_thing, look_for)
        if diff == 0:
            found_it = each_thing
            break
        elif diff < max_diff:
            max_diff = diff
            found_it = each_thing
    return (found_it)

print (find_closest(3.3, [1.5, 2.5, 4.5, 5.2, 6]))
print (find_closest(3.6, [1.5, 2.5, 4.5, 5.2, 6]))
print (find_closest(2.6, [1.5, 2.5, 4.5, 5.2, 6]))
#print (find_closest("59:59", ["59:29", "57:45", "59:03", "1:00:23", "1:01:45"]))

lst = ["59:29", "10:20"]
print(type(lst[0]))
