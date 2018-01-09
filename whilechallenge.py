import random

print("What number would you like to guess up to?")
highest = int(input())
answer = random.randint(1, highest)

print("You have 10 guesses to get the correct number\n")
print("Please guess a number between 1 and {}".format(highest))
guess = int(input())
guessCount = 0
while guess > highest:
    print("Please enter a valid number between 1 and {}".format(highest))
    guess = int(input())
if guess != answer:
    while guess != answer:
        if guess == 0:
            print("Come back when you want to play again")
            break
        guessCount += 1
        if guessCount == 3:
            print("If you want to stop guessing enter 0\n")
        if guessCount == 9:
            print("You have one more go!\n")
        if guessCount == 10:
            print("Game over! You've run out of guesses!\n")
            break
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")
        guess = int(input())
        if guess == answer:
            print("You have guessed correctly!")
else:
    print("You have guessed correctly first time!")
