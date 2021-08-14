import itertools
import operator
import functools

def findAll(nb_group, nums):
    size = sum(nums) // nb_group

    # On parcours tous les possibilites en fonction de la taille (Priorite taille plus petite pour le groupe 1).
    for i in range(len(nums) // nb_group + 2):
        qes = []
        
        # On cherche tous les combinaisons possible de cette taille dans la liste des nombres.
        for c in itertools.combinations(nums, i):

            # Si cela correspond a la bonne somme de sous groupe on calcule le quantum entanglement
            if sum(c) == size:
                qes.append(functools.reduce(operator.mul, c))

        # Si on a un quantum entanglement on renvoie la valeur minimal
        if qes:
            return min(qes)



nums = []
with open('input2.txt', 'r') as file:
    for row in file:
        nums.append(int(row.replace('\n','')))

print('Part 1:', findAll(3, nums))
print('Part 2:', findAll(4, nums))