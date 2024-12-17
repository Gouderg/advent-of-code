def ocr(A):
    out = []
    while A != 0:
        B = A % 8
        B = B ^ 3
        B = (A % 8) ^ 3
        C = A // 2**B
        B = B ^ 5
        A = A // 2**3
        B = B ^ C
        out.append(B%8)

    return out


def interval_to_test(int_l, int_r, prog, pos, seen):
    
    if ocr(int_l) == prog:
        if int_l not in seen:
            seen[int_l] = 0
        int_l += 1
        return seen
    if ocr(int_r) == prog:
        if int_r not in seen:
            seen[int_r] = 0
        int_r += 1
        return seen

    if pos < 0: return seen

    
    step = (int_r - int_l) // 8 + 1
    for i in range(0, 8):
        next_int_l = int_l + step*i
        next_int_r = int_l + step*(i+1)-1
    
        if ocr(next_int_l)[pos] == prog[pos]:
            seen = interval_to_test(next_int_l, next_int_r, prog, pos-1, seen)

    return seen

def main():
    prog = [2,4,1,3,7,5,1,5,0,3,4,3,5,5,3,0]
    first_seq = [7,5,6,2,3,0,1]
    interval_left, interval_right = 0, 0
    pos = len(prog)-1

    # First lap
    n = 8**pos
    n_1 = 8**(pos+1)-1
    step = (n_1 - n) // len(first_seq)
    f = first_seq.index(prog[pos])
    interval_left = interval_left + (n+f) + step*f
    interval_right = interval_right + (n+f+1) + step*(f+1) -1

    # Next 15 lap
    aled = interval_to_test(interval_left, interval_right, prog, pos-1, {})

    print("Part 2:", min(aled))

if __name__ == "__main__":
    main()



