entry = list('cqjxjnds')


# Part 1.
# Rule 1: 3 lettres consecutives.
# Rule 2: No i, o, l
# Rule 3: 2 time 2 sames letters consecutively with no-overlapping


def search(entry):
    while 1:
        
        # Incremente time.
        for j in range(len(entry)):
            if j+1 < len(entry) and ''.join(entry)[j+1:len(entry)] in 'zzzzzzzz':
                entry[j] = chr(((ord(entry[j]) - 97 + 1) % 26) + 97)
        entry[len(entry)-1] = chr(((ord(entry[len(entry)-1]) - 97 + 1) % 26) + 97)

        # On parcourt le liste a l'envers et si on tombe sur un i,l,o on lincremente.
        for j in range(0,len(entry)):
            if 'i' == entry[j] or 'l' == entry[j] or 'o' == entry[j]:
                entry[j] = chr(ord(entry[j])+1)
        
        # On cherche une succesion de trois lettres.
        isConsecutive = False
        for j in range(0,len(entry)):
            if j+2 < len(entry) and ord(entry[j]) == ord(entry[j+1]) - 1 and ord(entry[j]) == ord(entry[j+2]) - 2:
                isConsecutive = True
                break

        # On cherche 2*2 lettre en double sans overlapping.
        isDouble1, isDouble2, firstCarac = False, False, ''
        for j in range(0, len(entry)):
            if j+2 < len(entry) and entry[j] == entry[j+1] and entry[j] != entry[j+2] and firstCarac == '':
                firstCarac = entry[j]
                isDouble1 = True
            elif j+1 < len(entry) and entry[j] == entry[j+1] and firstCarac != entry[j]:
                if j+1 == len(entry)-1:
                    isDouble2 = True

        if isDouble1 and isConsecutive and isDouble2:
            return ''.join(entry)
            break
    
    
# Part 1.
first = search(list('cqjxjnds'))
print("Part 1:", first)
# Part 2.
print("Part 2:", search(list(first)))