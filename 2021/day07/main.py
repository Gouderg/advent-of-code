def solve(part):
    min_pos, min_fuel = 0, 20000000000
    for pos in range(1000):
        fuel = 0
        for row in data:
            if part == 1:
                fuel += abs(pos - row)
            else:
                fuel += (abs(pos - row) + 1) * (abs(pos - row)/2) 

        (min_pos,min_fuel) = (pos,int(fuel)) if fuel < min_fuel else (min_pos,min_fuel)
    
    return min_fuel

# Extract data.
data = []
with open('input.txt', 'r') as file:
    for row in file:
        data = [int(a) for a in row.replace('\n', '').split(',')]
        
# Part 1.
print('Part 1:', solve(1))

# Part 2.    
print('Part 2:', solve(2))