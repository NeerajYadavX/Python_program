import random
winning_number=random.randint(1,100)
guess=1
number=int(input("Guess a random number from 1 to 100: "))
game_over=False
while not game_over:
    if number==winning_number:
        print(f"YOU WIN !!!\nyou guessed this number in {guess} times\nnumber is {winning_number} ")
        game_over=True
    else:
        if number<winning_number:
            print("too low")
        else:
            print("too high")
    guess+=1
    number=int(input("guess again: "))
