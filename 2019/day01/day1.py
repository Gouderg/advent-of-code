
modules = []
fuel = 0

with open("input.txt", "r") as file:
    for data in file:
        modules.append(int(data))

for module in modules:
    while module > 0:
        module = module // 3 - 2
        if module > 0:
            fuel += module
print(fuel)
