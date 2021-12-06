from collections import Counter

def process(old_fish):
    new_fish = Counter()
    for i in range(6):
        new_fish[i] = old_fish[i+1]
    new_fish[6] = old_fish[0] + old_fish[7]
    new_fish[7] = old_fish[8]
    new_fish[8] = old_fish[0]
    return new_fish


def solve(data, iteration):
    lanternfish = Counter(data)
    for _ in range(0, iteration):
        lanternfish = process(lanternfish)
    return sum(lanternfish.values())


# Extract data.
data = []
with open('input.txt', 'r') as file:
    for row in file:
        data = [int(a) for a in row.replace('\n', '').split(',')]
        
# Part 1.
print('Part 1:', solve(data, 80))

# Part 2.
print('Part 2:', solve(data, 256))
