x = {"username": "admin", "machines": ["foo", "bar", "baz"]}
y = x.copy()

print (y)
y["machines"].remove("bar")
print (y)
print (x)

d = {}
d["names"] = ["Alfred", "Bertrand"]
c = d.copy()
from copy import deepcopy
dc = deepcopy(d)
d["names"].append("Clive")
print (c)
print (dc)
