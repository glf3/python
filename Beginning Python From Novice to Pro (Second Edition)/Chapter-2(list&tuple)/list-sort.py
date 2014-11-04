print (min(42, 32))
print (min(99, 100))
print (min(10, 10))

x = ["abwbwgaw", "abalone", "acme", "add", "aerate"]
x.sort(key=len)
print (x)

class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b


x = Test(10, 'x')
y = Test(2, 'y')
z = Test(3, 'z')

ans = min(x, y, z, key = lambda rhs:rhs.a)
print (ans.a, ans.b)

x = [1, 8, 9, 4, 3, 2, 6]
y = sorted(x)
print (x)
print (y)

