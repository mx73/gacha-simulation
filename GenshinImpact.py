import random
def GenshinImpact(pbase,pitynumber,n):
    #n=100
    repeat = 1000
    winrate = 0
    
    for o in range(repeat):
        wins = 0
        losses = 0
        current_losses= 0
        p=pbase
        
        for i in range(n):
            if random.random() < p:
                wins +=1
                p=pbase
            else:
                losses += 1
                current_losses +=1
                if current_losses > pitynumber:
                    p=1
                    current_losses = 0
        winrate = winrate + wins/n
    
    totalwinrate = winrate /repeat
    return totalwinrate