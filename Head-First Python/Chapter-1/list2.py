movies = ["The Holy Grail", 1975, "Terry Jones & Jerry Gilliam", 91,
["Graham Chapman", ["MichaelPalin", "John Cleese", "Terry Gilliam",
                                 "Eric Idle", "Tetty Jones"]]]

for item in movies:
    if isinstance(item, list):
        for item_iter in item:
            print (item_iter)
    else:
        print (item)

for each_item in movies:
    if isinstance(each_item, list):
        for nested_item in each_item:
            if isinstance(nested_item, list):
                for deeper_item in nested_item:
                    print (deeper_item)
            else:
                print(nested_item)
    else:
        print (each_item)
