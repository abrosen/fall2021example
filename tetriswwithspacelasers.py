import random
def autoRollTo20():
    total = 0
    while total < 20:
        roll = random.randint(1,6)
        #print("Roll:", roll)
        if roll == 1:
            total = 0
            #print("Turn total:", total)
            return total
        else:
            total = total + roll 
    #print("Turn total:", total)
    return total


def rollTo20Outcomes(numRuns):
    outcomes = {}
    for _ in range(numRuns):
        score = autoRollTo20()
        if score not in outcomes:
            outcomes[score] = 1
        else:
            outcomes[score] += 1
    return outcomes

n = 10000
outcomes = rollTo20Outcomes(n)
for score in sorted(outcomes):
    print(score, outcomes[score]/n ) 
