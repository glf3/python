x = [1, 1, 1]
x[1] = 2
print (x)

lst = [1, 2, 3]
lst.append(4)
print (lst)


c = ["to", "be", "or", "not", "to", "be"]
print (c.count("to"))

newx = [[1, 2], 1, 1, [2, 1, [1, 2]]]
print (newx.count([1, 2]))


a = [1, 2, 3]
b = [4, 5, 6]
print (a+b)
print (a) 
a.extend(b)
print (a)

a[len(a):] = b
print (a)

knights = ["We", "are", "the", "knights", "who", "say", "hi"]
print ("index is", knights.index("who"))

numbers = [1, 2, 3, 5, 6, 7]
numbers.insert(3, "four")
print (numbers)


x = [1, 2, 3]
print (x.pop())
print (x)

x = ["to", "be", "or", "not", "to", "be"]
change = input("input a string: ")
if change in x:
    x.remove(change)
    print ("remove successful")
    print (x)
else:
    print ("change is not in x")


x = [1, 2, 3]
print (x)
x.reverse()
print (x)


x = [4, 6, 2, 1, 7, 9]
y = x[:]
print ("befone sort: ", x)
x.sort()
print ("after sort: ", x)

y.sort()
print (y)
print (x)
