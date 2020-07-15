import random

def arknight(n):
    #n=100
    repeat = 1000
#    badluck = 0
#    blrate = 0
#    goodluck = 0
#    glrate = 0
#    totalwin = 0
    winrate = 0
    
    
    for o in range(repeat):
        wins = 0
        losses = 0
        current_losses= 0
        p=0.02
#        pmax=0.02
        for i in range(n):
            if random.random() < p:
                wins +=1
                current_losses = 0
#                if p > pmax:
#                    pmax = p
                p=0.02
            else:
                losses += 1
                current_losses += 1
                if current_losses > 49:
                    p+=0.02
            
        winrate = winrate + wins/n   
#        if pmax > 0.5:
#            badluck += 1
#            blrate = blrate + wins/n
#        else:
#            goodluck += 1
#            glrate = glrate + wins/n
        
    totalwinrate = winrate /repeat
    #totalbl = blrate / badluck
    #totalgl = glrate / goodluck
    return totalwinrate