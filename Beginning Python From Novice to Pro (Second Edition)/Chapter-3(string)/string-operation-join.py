seq = [1, 2, 3, 4, 5]
sep = "+"
"""
error operation
sep.join(seq)
"""

seq = ["1", "2", "3", "4", "5"]
sep = "+"
print (sep.join(seq))

dirs = "", "usr", "bin", "env"
print ("/".join(dirs)) #Linux

print ("C:" + "\\".join(dirs)) #Windows

