width = input("Please enter width: ")

price_width = 10
tmp = width
tmp = int(tmp)
item_width = tmp - price_width

header_format = "%-*s%*s"
format = "%-*s%*.2f"

print ("=" * tmp)
print (header_format % (item_width, "Item", price_width, "Price"))
print ("-" * tmp)

print (format % (item_width, "Apples", price_width, 0.4))
print (format % (item_width, "Pears", price_width, 0.5))
print (format % (item_width, "Cantaloupes", price_width, 1.92))
print (format % (item_width, "Dried Apricots (16 oz.)", price_width, 8))
print (format % (item_width, "Prunes (4 libs.)", price_width, 12))
print ("=" * tmp)
