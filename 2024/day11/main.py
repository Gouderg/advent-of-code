# Part 2.
stones = {}

with open("input.txt", "r") as file:
    for row in file:
        row = [int(a) for a in list(row.replace("\n", "").split(" "))]
        for a in row:
            stones[a] = 1

memory = {0: 1}

for i in range(75):
    if i == 25:
        print("Part 1:", sum([stones[a] for a in stones]))

    new_stones = {}
    for s in stones:
        if s in memory:
            if isinstance(memory[s],list):
                if memory[s][0] not in new_stones:
                    new_stones[memory[s][0]] = 0
                if memory[s][1] not in new_stones:
                    new_stones[memory[s][1]] = 0
                new_stones[memory[s][0]] += stones[s]
                new_stones[memory[s][1]] += stones[s]
            else:
                if memory[s] not in new_stones:
                    new_stones[memory[s]] = 0
                new_stones[memory[s]] += stones[s]

            continue

        if len(str(s)) % 2 == 0:
            str_stones = str(s)
            left, right = int(str_stones[0:len(str_stones)//2]), int(str_stones[len(str_stones)//2:])
            memory[s] = [left, right]
            if isinstance(memory[s],list):
                if memory[s][0] not in new_stones:
                    new_stones[memory[s][0]] = 0
                if memory[s][1] not in new_stones:
                    new_stones[memory[s][1]] = 0
                new_stones[memory[s][0]] += stones[s]
                new_stones[memory[s][1]] += stones[s]
            else:
                if memory[s] not in new_stones:
                    new_stones[memory[s]] = 0
                new_stones[memory[s]] += stones[s]


        else:
            memory[s] = s*2024
            if isinstance(memory[s],list):
                if memory[s][0] not in new_stones:
                    new_stones[memory[s][0]] = 0
                if memory[s][1] not in new_stones:
                    new_stones[memory[s][1]] = 0
                new_stones[memory[s][0]] += stones[s]
                new_stones[memory[s][1]] += stones[s]
            else:
                if memory[s] not in new_stones:
                    new_stones[memory[s]] = 0
                new_stones[memory[s]] += stones[s]


    stones = new_stones.copy()

print("Part 2:", sum([stones[a] for a in stones]))

