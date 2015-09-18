movies = ["The Holy Grail", "The Life of Brian", "The Meaning of Life"]
print (movies[1])

cast = ["Cleese", "Palin", "Jones", "Idle"]
print(cast)
print(len(cast))
print(cast[1])

cast.append("Gillam")
print (cast)
cast.pop()
print (cast)
cast.extend(["Gilliam", "Chapman"])
print (cast)
cast.remove("Chapman")
print (cast)
cast.insert(0, "Chapman")
print (cast)

"""
    Way 1
"""
length = len(movies)
movies2 = movies
p = 1
for i in range(length):
    year = int(input("Input a interger:"))
    movies2.insert(p, year)
    p += 2
print(movies2)

"""
    Way2
"""
movies3 = ["The Holy Grail", 1975,
          "The life of Brian", 1979,
          "The Meaning of Life", 1983]
print (movies3)

movies = ["The Holy Grail", "The Life of Brian", "The Meaning of Life"]
print (movies)
count = 0
while count < len(movies):
    print (movies[count])
    count += 1

names = ["Michael", "Terry"]
print (isinstance(names, list))
num_names = len(names)
print (isinstance(num_names, list))


movies = ["The Holy Grail", 1975, "Terry Jones & Jerry Gilliam", 91,
["Graham Chapman", ["MichaelPalin", "John Cleese", "Terry Gilliam"
                                 "Eric Idle", "Tetty Jones"]]]
print (movies)
