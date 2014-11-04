website = "http://glf3.i11r.com"
print (website[-3:])


format1 = "Hello, %s. %s enough for ya?"
values = ("world", "hot")
print (format1 % values)

x = "world"
y = "hot"
print ("Hello, %s. %s enough for ya?" % (x, y))


format1 = "Pi with three decimal: %.3f"
from math import pi
print (format1 % pi)


from string import Template
s = Template("$x, It's glorious $x!")
print (s.substitute(x = 'slum'))


print ("%s plus %s equals %s" % (1, 1, 2))

#print ("%s plus %s equals %s" % 1, 1, 2) # Lacks parentheses!

print ("Price of eggs: $%d" % 42)

from math import pi
print ("Pi is %.3f" % pi)

print ("%010.2f" % pi)

print ("%-10.2f %d" % (pi, 4))

print ("%.*s" % (5, "Guido van Rossum"))

print ("%+5d" % 10)
print ("%+5d" % -10)
