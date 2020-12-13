from functools import reduce
'''
    Exemple (tiré de Han Xin Counting Off Algorithm)
        x ≡ 2 mod(3)
        x ≡ 3 mod(5)
        x ≡ 2 mod(7)
    
    n = [3,5,7] => n_i termes
    a = [2,3,2] => a_i termes

    N = Somme des n_i termes = 3 * 5 * 7 = 105
    n_1 = 3 -> N1_inv = N / n_1

    Pour calculer le coefficient devant le N1_inv on utilise le théorème de Bachet-Bézout: ax + by = pgcd(a)
    Or ici on a u_i * n_i + v_i * ni_inv = pgcd(u_i, v_i)   => on cherche v_i modulo n_i (il doit être positif)
    On utile l'algorithme d'euclide étendu et on a la fonction mul_inv
'''

def chinese_remainder(n, a):
    somme = 0
    N = reduce((lambda a, b: a*b), n)  # Multiplie tous les ni termes entre eux pour avoir n
    
    for n_i, a_i in zip(n,a):
        Ni_inv = N / n_i
        somme += a_i * mul_inv(Ni_inv, n_i) * Ni_inv
    return round(somme % N)

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1<0 : x1 += b0     # Si on lui rajoute n_i pour qu'il ne soit pas négatif (il le sera forcément sinon l'équation n'est pas respecté)
    return x1


if __name__ == "__main__":
    
    data = []

    with open("input.txt","r") as file:
        for row in file:
            row = row.replace('\n', '')
            data.append(row)
    
    ## Part 1
    depart, time = int(data[0]), []
    
    for elt in data[1].split(','):
        if elt != 'x':
            time.append(int(elt))

    nbProche, ids = depart**2, 0
    for elt in time:
        temp = ((depart // elt) + 1) * elt

        if nbProche > temp:
            nbProche = temp
            ids = elt
    
    print("Part 1:", (nbProche - depart) * ids)

    ## Part 2

    depart = int(data[0])

    n, a, couple = [], [], []
    for i,elt in enumerate(data[1].split(',')):
        if elt != 'x':
            couple.append((int(i), int(elt)))
    
    
    for i, m in couple:
        a.append(-i % m)
        n.append(m)
        #print("x = {} mod {}".format(-i % m,m))
    
    print("Part 2:", chinese_remainder(n,a))
