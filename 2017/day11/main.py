# Big love to : https://www.redblobgames.com/grids/hexagons/

# Extract data.
data = []
with open("input.txt", "r") as file:
    for row in file:
        data = row.replace("\n", "").split(",")

print(data)

i, j = 50, 50
for elt in data:
    if elt == "nw":
        i -= 1
        j -= 1
    elif elt == "n":
        i -= 1
    elif elt == "ne":
        i -= 1
        j += 1
    elif elt == "sw":
        pass
    elif elt == "s":
        pass
    elif elt == "se":
        pass

'''
Even q
    1,0
0,0     2,0
    1,1 
0,1     2,1
    1,2
'''

