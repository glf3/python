try:
    data = open("missing.txt")
    print(data.readline(), end="")
except IOError:
    print("File Error")
finally:
    data.close()
