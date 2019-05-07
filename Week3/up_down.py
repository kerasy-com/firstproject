import random

chances = 5
random_number = random.randrange(1, 51)
min = 1
max = 50

while chances > 0:
    choice = int(input("Guess the random number(range: {0} ~ {1}): ".format(min, max)))

    if chances == 0:
        print("Your chances ran out! Too bad.\n")
        print("The number was... : {0}".format(random_number))

    if choice == random_number:
        print("You got the random number! You win!")
        break
    else:
        chances -= 1
        if choice > random_number:
            print("Down")
            max = choice
        else:
            print("Up")
            min = choice
        print("Now you got {0} chances~!".format(chances))

if(chances ==0 ):
    print("You suck at this game! The number was:", random_number)