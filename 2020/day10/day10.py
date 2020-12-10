
if __name__ == "__main__":
    
    data = []

    with open('input.txt', 'r') as file:
        for row in file:
            row = row.replace('\n', '')
            data.append(int(row))
        data.append(max(data) + 3)
        data.append(0)

    ## Part 1
    diff1jolt, diff3jolt, previousValue = 0, 0, 0
    data.sort()

    for value in data:
        if value == previousValue + 1:
            diff1jolt += 1
        
        elif value == previousValue + 3:
            diff3jolt += 1
        previousValue = value

    print("Part 1:", diff1jolt * diff3jolt)

    ## Part 2 
    # Thanks to Aurélien Simon - https://github.com/aureliensimon 
    routes = [0] * (max(data) + 1)
    routes[0] = 1

    for i in data:
        routes[i] += routes[i-1] + routes[i-2] + routes[i-3]

    print("Part 2:", routes[len(routes)-1])


