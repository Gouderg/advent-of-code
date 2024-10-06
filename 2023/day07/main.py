
from collections import Counter
data = {}

with open("input.txt", "r") as file:

    for row in file:
        hand, bid = row.replace("\n", "").split(" ")
        data[hand] = int(bid)


card_value = {
    'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10,
    '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4,
    '3': 3, '2': 2, '1': 1 
}

def compare_bit_to_bit(a, b):
    """ Return true if a > b else False """
    for i in range(0, 5):
        if card_value[a[i]] == card_value[b[i]]: continue

        return card_value[a[i]] > card_value[b[i]]


def build_map(a):
    """ Get """

    counts = Counter(a)
    five_kind, four_kind, triple, nb_pair = False, False, False, 0
    
    cpt = 0
    for count in counts:
        if counts[count] == 5: five_kind = True
        if counts[count] == 4: four_kind = True
        if counts[count] == 3: triple = True
        if counts[count] == 2: nb_pair += 1

    if five_kind: cpt = 6
    elif four_kind: cpt = 5
    elif triple and nb_pair == 1: cpt = 4
    elif triple: cpt = 3
    else: cpt = nb_pair 

    return cpt




# Part 1.
hands = {}
keys = list(data.keys())
for hand in keys:
    hands[hand] = build_map(hand)

def compare(a, b):
    v1, v2 = hands[a], hands[b]

    if v1 == v2: return compare_bit_to_bit(a, b)

    return v1 > v2


j = 0
for i in range(1, len(keys)):
    a = keys[i]
    j = i-1
    while j >= 0 and compare(keys[j], a):
        keys[j+1] = keys[j]
        j -= 1
    keys[j+1] = a

somme = 0
for rank, hand in enumerate(keys):
    somme += (rank+1) * data[hand]



print("Part 1:", somme)