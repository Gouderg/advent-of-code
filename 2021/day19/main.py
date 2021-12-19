import itertools
import math


# Extract data.
scanners = {}
with open("input2.txt", "r") as file:
    for row in file:
        if "scanner" in row:
            row = row.replace('\n', '').split(' ')
            id_scanner = int(row[2])
            if id_scanner not in scanners:
                scanners[id_scanner] = []
        elif "," in row:
            row = [int(a) for a in row.replace('\n', '').split(',')]
            scanners[id_scanner].append(row)

# Part 1.

print("Part 1:", "Aled")