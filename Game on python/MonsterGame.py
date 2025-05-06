# FILE FOR GAME

# RAISE A MONSTER: IF FOOD, TRAIN, OR REST CONDITION IS MET: DISPLAY DIALOGUE

# DIALOGUE CHANGES DEPENDING ON CONDITION

import GameModel as gm

def greetingMessage():              # Greets user to the game
    print('Welcome to My Mini Monster')
    print('This is a game about picking and raising a monster ' \
          'however you choose.')
    print()
    input('(Press enter to continue)')
    print()
    
def getMonsterChoice():             # Asks user which monster they'd like to choose
    while True:
        try:
            myMonster = input('Choose the number of the monster you\'d like ' \
                              'to select as you see it on the menu: ')
        except Exception:
            print('You must choose a monster to continue!')
            continue
        if myMonster not in['1', '01', '2', '02', '3', '03']:
            continue
        else:
            break
    if myMonster == '1' or myMonster == '01':
        myMonster = 'Slime Blob'
    elif myMonster == '2' or myMonster == '02':
        myMonster = 'Calamari Critter'
    elif myMonster == '3' or myMonster == '03':
        myMonster = 'Eye..?'
    return myMonster

def getActivityChoice():            # Asks user which activity they'd like their monster to perform
    while True:
        try:
            choice = input('Do you want to:\n' \
                   '(F) Feed your monster\n' \
                   '(T) Train your monster\n' \
                   '(R) Rest your monster?: ').casefold()
        except Exception:
            print('You must choose an option!')
            continue
        if choice not in['f', 't', 'r']:
            continue
        else:
            break
    return choice

def isMonsterSlimeBlob(choice):         # All 3 monster functions kinda do the same thing with diff values,
    feedCount = 0                       # could possibly make a single function that takes diff values, etc.
    trainCount = 0
    restCount = 0
    while (feedCount < 5) or (trainCount < 4) or (restCount < 3):
        while (choice == 'f'):
            feedCount = trackFeedCount(feedCount, MAXFEEDCOUNT = 5)
            if feedCount < 5:
                print()         # All these choice inputs are redundant and I could use getActivityChoice()
                choice = input('Do you want to:\n' \
                               '(F) Feed your monster again\n' \
                               '(T) Train your monster\n' \
                               '(R) Rest your monster?: ').casefold()
                print()
                if choice != 'f':
                    break
            elif feedCount == 5:
                print()
                gm.monsterSlimeBlobDialogue(choice)
                return
        while choice == 't':
            trainCount = trackTrainCount(trainCount, MAXTRAINCOUNT = 4)
            if trainCount < 4:
                print()
                choice = input('Do you want to:\n' \
                               '(F) Feed your monster\n' \
                               '(T) Train your monster again\n' \
                               '(R) Rest your monster?: ').casefold()
                print()
                if choice != 't':
                    break
            elif trainCount == 4:
                print()
                gm.monsterSlimeBlobDialogue(choice)
                return
        while choice == 'r':
            restCount = trackRestCount(restCount, MAXRESTCOUNT = 3)
            if restCount < 3:
                print()
                choice = input('Do you want to:\n' \
                               '(F) Feed your monster\n' \
                               '(T) Train your monster\n' \
                               '(R) Rest your monster again?: ').casefold()
                print()
                if choice != 'r':
                    break
            elif restCount == 3:
                print()
                gm.monsterSlimeBlobDialogue(choice)
                return
def isMonsterCalamariCritter(choice):
    feedCount = 0
    trainCount = 0
    restCount = 0
    while (feedCount < 6) or (trainCount < 5) or (restCount < 8):
        while (choice == 'f'):
            feedCount = trackFeedCount(feedCount, MAXFEEDCOUNT = 6)            
            if feedCount < 6:
                print()
                choice = input('Do you want to:\n' \
                               '(F) Feed your monster again\n' \
                               '(T) Train your monster\n' \
                               '(R) Rest your monster?: ').casefold()
                print()
                if choice != 'f':
                    break
            elif feedCount >= 6:
                print()
                gm.monsterCalamariCritterDialogue(choice)
                return
        while choice == 't':
            trainCount = trackTrainCount(trainCount, MAXTRAINCOUNT = 5)
            if trainCount < 5:
                print()
                choice = input('Do you want to:\n' \
                               '(F) Feed your monster\n' \
                               '(T) Train your monster again\n' \
                               '(R) Rest your monster?: ').casefold()
                print()
                if choice != 't':
                    break
            elif trainCount == 5:
                print()
                gm.monsterCalamariCritterDialogue(choice)
                return
        while choice == 'r':        
            restCount = trackRestCount(restCount, MAXRESTCOUNT = 8)            
            if restCount < 8:
                print()
                choice = input('Do you want to:\n' \
                               '(F) Feed your monster\n' \
                               '(T) Train your monster\n' \
                               '(R) Rest your monster again?: ').casefold()
                print()
                if choice != 'r':
                    break
            elif restCount == 8:
                print()
                gm.monsterCalamariCritterDialogue(choice)
                return
def isMonsterEye(choice):  
    feedCount = 0
    trainCount = 0
    restCount = 0
    while (feedCount < 8) or (trainCount < 6) or (restCount < 10):
        while (choice == 'f'):
            feedCount = trackFeedCount(feedCount, MAXFEEDCOUNT = 8)
            if feedCount < 8:
                print()
                choice = input('Do you want to:\n' \
                               '(F) Feed your monster again\n' \
                               '(T) Train your monster\n' \
                               '(R) Rest your monster?: ').casefold()
                print()
                if choice != 'f':
                    break
            elif feedCount >= 8:
                print()
                gm.monsterEyeDialogue(choice)
                return
        while choice == 't':
            trainCount = trackTrainCount(trainCount, MAXTRAINCOUNT = 6)
            if trainCount < 6:
                print()
                choice = input('Do you want to:\n' \
                               '(F) Feed your monster\n' \
                               '(T) Train your monster again\n' \
                               '(R) Rest your monster?: ').casefold()
                print()
                if choice != 't':
                    break
            elif trainCount == 6:
                print()
                gm.monsterEyeDialogue(choice)
                return
        while choice == 'r':
            restCount = trackRestCount(restCount, MAXRESTCOUNT = 10)
            if restCount < 10:
                print()
                choice = input('Do you want to:\n' \
                               '(F) Feed your monster\n' \
                               '(T) Train your monster\n' \
                               '(R) Rest your monster again?: ').casefold()
                print()
                if choice != 'r':
                    break
            elif restCount == 10:
                print()
                gm.monsterEyeDialogue(choice)
                return
def trackFeedCount(feedCount, MAXFEEDCOUNT):
    feedQuantity = gm.doFeed(feedCount, MAXFEEDCOUNT)
    feedCount += feedQuantity
    return feedCount
def trackTrainCount(trainCount, MAXTRAINCOUNT):
    trainQuantity = gm.doTrain(trainCount, MAXTRAINCOUNT)
    trainCount += trainQuantity
    return trainCount
def trackRestCount(restCount, MAXRESTCOUNT):
    restQuantity = gm.doRest(restCount, MAXRESTCOUNT)
    restCount += restQuantity
    return restCount
def main():
    greetingMessage()
    gm.printMonsterMenu()
    myMonster = getMonsterChoice()
    choice = getActivityChoice()
    print()
    if myMonster == 'Slime Blob':
        isMonsterSlimeBlob(choice)
    elif myMonster == 'Calamari Critter':
        isMonsterCalamariCritter(choice)
    elif myMonster == 'Eye..?':
        isMonsterEye(choice)
        
main()
