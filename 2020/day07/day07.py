def explore(tab, key):
    if tab[key] == {}:
        return 1
    else:
        nbSac = 0
    
    for elt in tab[key]:
        nbSac += tab[key][elt] * explore(tab, elt)
        if explore(tab,elt) != 1:
            nbSac += tab[key][elt]
    return nbSac

if __name__ == "__main__":
    data = []

    with open("input.txt","r") as file:
        for row in file:
            row = row.replace('\n','')
            data.append(row)

    ## Part 1
    specify_color = ['shiny gold']

    for colors in specify_color:
        for row in data:
            row = row.split('contain')
            if colors in row[1]:
                newColor = row[0].split(' bags')
                if newColor[0] not in specify_color:
                    specify_color.append(newColor[0])

    print("First Star:", len(specify_color)-1)

    ## Part 2

    specify_color = ['shiny gold']
    parent = dict()

    for colors in specify_color:
        for row in data:
            row = row.split('contain')
            if colors in row[0]:
                setColor = row[1].split(', ')
                temp = dict()
                for part in setColor:
                    part = part.replace('.','')
                    if 'bags' in part:
                        part = part.replace(' bags', '')
                    elif 'bag' in part:
                        part = part.replace(' bag', '')
                    if 'no other' not in part:
                        part = part.split()
                        temp[part[1]+' '+part[2]] = int(part[0])
                        if part[1]+' '+part[2] not in specify_color:
                            specify_color.append(part[1]+' '+part[2])
                parent[colors] = temp

    print("Second Star:", explore(parent,'shiny gold'))
