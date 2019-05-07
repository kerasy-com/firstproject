import random

class num_baseball():
    cipher_num = 0
    chances = 5
    answer_number = "0"
    strikes = 0
    balls = 0

    def __init__(self, cipher_num):
        self.cipher_num = cipher_num
        self.answer_number = str(random.randrange(10**(self.cipher_num-1), 10**(self.cipher_num)))
    
    def how_many_strikes(self, guess):
        guess = str(guess)
        for i in range(0, len(self.answer_number)):
            if(self.answer_number[i] == guess[i]):
                self.strikes += 1

        return self.strikes
    
    def how_many_balls(self, guess):
        guess = str(guess)
        for i in guess:
            if i in self.answer_number:
                self.balls += 1

        return (self.balls - self.strikes)

    def print_result(self, guess):
        self.strikes = self.how_many_strikes(guess)
        self.balls = self.how_many_balls(guess)

        if self.strikes == self.cipher_num:
            print("You got it right! The number was: {}".format(self.answer_number))
            return 0
            
        elif (self.balls == 0) and (self.strikes == 0):
            print("Out! Guess again!")
            self.chances -= 1
        else:
            print("You got {} strikes and {} balls!".format(self.strikes, self.balls))
            self.chances -= 1
        
        if self.chances == 0:
            print("Haha, you suck! The real number was: {}".format(self.answer_number))
            return -1
        
        self.reset_numbers()
        return 1
    
    def reset_game(self):
        self.answer_number = str(random.randrange(10^self.cipher_num, 10^(self.cipher_num+1)))
        self.chances = 5
    
    def reset_numbers(self):
        self.balls = 0
        self.strikes = 0

cipher_num = int(input("What do you want as a cipher number? : "))
new_game = num_baseball(cipher_num)
print(new_game.answer_number)
guess = int(input("What is your guess? : "))

while new_game.print_result(guess) == 1:
    guess = int(input("What is your guess? : "))
    