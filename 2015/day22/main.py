def battle(actions, part):
    boss = {'hit': 55, 'damage': 8}
    hero = {'hit': 50, 'mana': 500, 'armor': 0, 'poison': 0, 'shield': 0, 'recharge': 0}
    
    turn, turn_c = 0, 0
    mana_spent = 0
    my_turn = True
    spell_cost = {'M': 53, 'D': 73, 'S': 113, 'P': 173, 'R': 229}
    
    while True:
        
        # Spell Poison.
        if hero['poison']:
            hero['poison'] -= 1
            boss['hit'] -= 3
        
        # Spell Shield.
        hero['armor'] = 7 if hero['shield'] else 0
        hero['shield'] = hero['shield'] - 1 if hero['shield'] else 0
      
        # Spell Recharge.  
        if hero['recharge']:
            hero['recharge'] -= 1
            hero['mana'] += 101
        
        if my_turn:
            
            # Part 2.
            if part == 2:
                hero['hit'] -= 1
                if hero['hit'] <= 0: return 0

            hero['mana'] -= spell_cost[actions[turn_c]]
            mana_spent += spell_cost[actions[turn_c]]
            
            if actions[turn_c] == 'M':
                boss['hit'] -= 4
            
            elif actions[turn_c] == 'D':
                boss['hit'] -= 2
                hero['hit'] += 2
            
            elif actions[turn_c] == 'S':
                if hero['shield']: return 0
                hero['shield'] = 6
            
            elif actions[turn_c] == 'P':
                if hero['poison']: return 0
                hero['poison'] = 6
            
            elif actions[turn_c] == 'R':
                if hero['recharge']: return 0
                hero['recharge'] = 5
            
            if hero['mana'] < 0: return 0
        
        if boss['hit'] <= 0: return mana_spent
        
        if not(my_turn):
            hero['hit'] -= max(boss['damage'] - hero['armor'], 1)
            if hero['hit'] <= 0: return 0
        
        turn_c = turn_c + 1 if my_turn else turn_c
        my_turn = not(my_turn)
        turn += 1

def findSpell(pos):
    actions[pos] = 'DSPRM'['MDSPR'.index(actions[pos])]
    if actions[pos] == 'M'and pos+1 <= len(actions):
        findSpell(pos+1)

# Part 1 & 2.
for i in (1,2):
    actions, mana = ['M'] * 20, 100000
    for _ in range(140000):
        result = battle(actions, i)
        if result > 0 and result < mana:
            mana = result
        findSpell(0)    

    print('Part {}: {}'.format(i, mana))