import random

def how_many_strike(number, guess):
    strike = 0
    for i in range(0, len(number)):
        if(number[i] == guess[i]):
            strike += 1
    return strike

def how_many_balls(number, guess):
    balls = 0
    for item in guess:
        if item in number:
            balls += 1
    return (balls - how_many_strike(number, guess))

number = str(random.randrange(100, 1000))
print(number)
chances = 5

while chances > 0:
    print("You got", chances, "chances left!")
    guess = input("What is your guess? : ")

    balls = how_many_balls(str(number), str(guess))
    strike = how_many_strike(str(number), str(guess))

    if strike == 3:
        print("You got it right! The number was: ", number)
        break
    elif (balls == 0) and (strike == 0):
        print("Out! Guess again!")
        chances -= 1
    else:
        print("You got ", strike, " strike and ", balls, " ball!")
        chances -= 1
    
if chances == 0:
    print("Haha, you suck! The real number was: ", number)
