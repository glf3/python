def print_lol(the_list, indent = false, level=0):
    for item in the_list:
        if isinstance(item, list):
            print_lol(item, level+1)
        else:
            if indent:
                for i in range(level):
                    print ("\t", end="")
            print (item)


def print_lol(the_list, indent = false, level=0, fh = sys.stdout):
    for item in the_list:
        if isinstance(item, list):
            print_lol(item, indent, level+1, fh)
        else:
            if indent:
                for i in range(level):
                    print ("\t", end="", file = fh)
            print (item, file = fh)


def print_lol(the_list, indent = false, level=0, fh = sys.stdout):
    for item in the_list:
        if isinstance(item, list):
            print_lol(item, indent, level+1, fh)
        else:
            if indent:
                for i in range(level):
                    print ("\t", end="", file = fh)
            print (item, file = fh)


            
