from tqdm import tqdm

# Parse data.
data = []
with open("input.txt", "r") as file:
    for row in file:
        row = int(row.replace("\n", ""))
        data.append(row)

def step(secret):
    secret = (secret ^ (secret * 64)) % 16777216 
    secret = (secret ^ (secret // 32)) % 16777216
    secret = (secret ^ (secret * 2048)) % 16777216
    return secret

# Part 1.
cpt = 0

for secret in data:
    for i in range(2000):
        secret = step(secret)
    cpt += secret

print("Part 1:", cpt)

# Part 2.
seq_tot = {}
for secret in tqdm(data, total=len(data)):

    buyer = [secret % 10]
    
    for _ in range(2000):
        secret = step(secret)
        buyer.append(secret % 10)
    
    seen = set()
    for i in range(len(buyer)-4):
        a, b, c, d, e = buyer[i:i+5]
        seq = (b-a, c-b, d-c, e-d)
        if seq in seen: continue
        seen.add(seq)
        if seq not in seq_tot:
            seq_tot[seq] = 0
        seq_tot[seq] += e

print("Part 2:", max(seq_tot.values()))