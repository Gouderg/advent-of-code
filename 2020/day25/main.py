def find_loop_size_without_number(key):
    number, nb = 2, 2
    loop = 1
    while True:
        loop += 1
        number = (number*nb) % 20201227

        if key == number:
            return loop, nb
        elif number > key:
            nb += 1
            number = nb 
            loop = 1

def find_loop_size_with_number(number, key):
    loop = 1
    nb = number
    while True:
        loop += 1
        number = (number * nb) % 20201227

        if key == number:
            return loop

def handshake(nb, key, loop):
    for _ in range(0,loop):
        key = (key * 7) % 20201227
    return key


# Extract input.
card_key, door_key = 5764801, 17807724
loop_card, subject_number = find_loop_size_without_number(card_key)
loop_door = find_loop_size_with_number(subject_number, door_key)

print(subject_number, card_key, loop_card, door_key, loop_door)
print("Part 1:", handshake(card_key, card_key, loop_door))
