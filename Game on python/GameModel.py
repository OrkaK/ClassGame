#   MODULE TO BE IMPORTED
#   5 FUNCTIONS, 3 MUST RETURN

def doFeed(feedCount, MAXFEEDCOUNT):   # Return func
    feedQuantity = 0
    while True:
        try:
            feedQuantity = int(input(f'How many times do you want to feed your monster ' \
                                     f'(1 - {MAXFEEDCOUNT - feedCount}): '))
        # when feedCount = 4 theres a weird bug that i cant fix, input asks for user to enter a value in a range (1, 1)
        except ValueError:              
            print('You must enter a valid integer!')
            continue 
        if feedQuantity < 0 or feedQuantity > MAXFEEDCOUNT:
            print(f'You must choose a value within the range 1 - {MAXFEEDCOUNT - feedCount}!')
            continue
        elif feedQuantity > MAXFEEDCOUNT - feedCount:                   # if value = 'x', user can not input a value
            print(f'You must choose a value within the range 1 - {MAXFEEDCOUNT - feedCount}!')  # greater than MAX - count
            continue
        else:                                                                                    
            break

    return feedQuantity

def doTrain(trainCount, MAXTRAINCOUNT):  # Return func
    trainQuantity = 0
    while True:
        try:
            trainQuantity = int(input(f'How many times do you want to train your monster ' \
                                      f'(1 - {MAXTRAINCOUNT - trainCount}): '))
        except ValueError:
            print('You must enter a valid integer!')
        if trainQuantity < 0 or trainQuantity > MAXTRAINCOUNT:
            print(f'You must choose a value within the range 1 - {MAXTRAINCOUNT - trainCount}!')
            continue
        elif trainQuantity > MAXTRAINCOUNT - trainCount:
            print(f'You must choose a value within the range 1 - {MAXTRAINCOUNT - trainCount}!')
            continue
        else:
            break
    return trainQuantity
    
def doRest(restCount, MAXRESTCOUNT):    # Return func
    restQuantity = 0
    while True:
        try:
            restQuantity = int(input(f'How many times do you want to rest your monster ' \
                                      f'(1 - {MAXRESTCOUNT - restCount}): '))
        except ValueError:
            print('You must enter a valid integer!')
        if restQuantity < 0 or restQuantity > MAXRESTCOUNT:
            print(f'You must choose a value within the range 1 - {MAXRESTCOUNT - restCount}!')
            continue
        elif restQuantity > MAXRESTCOUNT - restCount:
            print(f'You must choose a value within the range 1 - {MAXRESTCOUNT - restCount}!')
            continue
        else:
            break
    return restQuantity
    
def printMonsterMenu():                 # Print func
    monsters = ['Slime Blob', 'Calamari Critter', 'Eye..?']
    print('', format('Monster Menu', '^31'))
    print()
    for count in range(len(monsters)):
        print(f'{count+1:02d}', end='\t')
        print(monsters[count])
    print()
    
def monsterSlimeBlobDialogue(choiceEnding): # Print Slime Blob Dialogue
    if choiceEnding == 'f':
        print('Your slime blob has grown to an incredible size! ' \
              'It\'s decided to take the job of the Town\'s biggest ' \
              'bouncy house, great for both kids & adults alike!')
    elif choiceEnding == 't':
        print('Your slime blob tried to keep up with your training, but it! ' \
              ' overheated and melted. What once was, is now an unrecognizable ' \
              ' puddle. ')
    else:
        print('Slime blob has rested so much, it has decided that society\'s mold ' \
              'is too restrictive. It has decided to " go with the flow" '\
              'and now won\'t hold any shape you tell it to.')
    
def monsterCalamariCritterDialogue(choiceEnding):   # Print Calamari Critter Dialogue
    if choiceEnding == 'f':
        print('Your monster grows into the biggest squid the town has ' \
              'ever seen! But while you were sleeping, the local fishermen ' \
              ' decided to poach him... Your calamari critter is now a' \
              'delicious fritter! ')
    elif choiceEnding == 't':
        print('You trained with your monster so much that it has now transformed ' \
              'into a powerful monster, reviered king of the sea! ' \
              'It isn\'t home very much, but once in a while you hear ' \
              'local pirates talk about lost crews, with the last thing ' \
              'they see being a great tentacle.')
    else:
        print('While your monster was resting, it accidentally laid down ' \
              'suction cup first. It has spent too much time asleep, ' \
              'so when you attempted to wake it up, it was permanently '\
              'stuck to the ground')

def monsterEyeDialogue(choiceEnding):           # Print Eye Dialogue
    if choiceEnding == 'f':
        print('It has managed to absorb all the food given to it. '\
              'Your eye grew too big and popped out of his socket! ' \
              'You tried to pop it back in but to no avail...')
    elif choiceEnding == 't':
        print('Your eye has picked up training impressively fast, ' \
              'gaining tremendous amounts of strength. The only problem ' \
              'now is everytime it blinks, it creates a giant gust of' \
              'wind; blowing you away. It\'s virtually impossible for you' \
              'to stand in a 20ft radius of your monster. ')
    else:
        print('After laying dormant for a significant amount of time ' \
              'the eye begins to glow. After a flash of blinding light, ' \
              'you notice that your monster has evolved,  all it says is\n\n' \
              'ኃጢአተኛ ነፍስህ ከመዳን በላይ ናት እናም ሰላምን ወይም ' \
              'ሥቃይን አታውቅም ፣ የንስሐ ቅዝቃዜ ብቻ አብቅቷል ፣ ምክንያቱም ' \
              'ኃጢአቶችህ ከማንኛውም ተልእኮ የላቀ ስለሆነ ፣ መጨረሻው ቀርቧል ፣ የኃጢአት መርከቦች \n\n' \
              'It\'s now way past your capabilities of understanding, but at '\
              'least you\'re ready for the rapture. ')
