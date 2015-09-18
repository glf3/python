movies = ["The Holy Grail", 1975, "Terry Jones & Jerry Gilliam", 91,
["Graham Chapman", ["MichaelPalin", "John Cleese", "Terry Gilliam",
                                 "Eric Idle", "Tetty Jones"]]]

def print_lol(the_list):
    for item in the_list:
        if isinstance(item, list):
                print_lol(item)
        else:
            print (item)

print_lol(movies)
