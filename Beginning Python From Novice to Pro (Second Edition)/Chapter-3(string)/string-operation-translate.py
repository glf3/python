table = str.maketrans("cs", "kz")

string = "this is an incredible test"
string.translate(table)
print (string)
print (string.translate(table))

s = string.translate(table)
