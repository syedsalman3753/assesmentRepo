inventory = {
    "fruits": {"apples": 10, "oranges": 5},
    "vegetables": {"carrot": 7, "beans": 4}
}

##
##Char    item   quantity
#3fruits  app     10

for c in inventory:
    for i in inventory[c]:
        if inventory[c][i]>5:
            print(c," ",i," ",inventory[c][i])
