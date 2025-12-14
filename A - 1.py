import random
play=True
n=str(random.randint(10,20))
print("Lets guess numbers between 10 and 20")
print("The game ends when you guess the correct number")
while play:
    guess=input("Guess the Number: ")
    if guess == n:
        print("You guessed it right")
        print("The numbe rwas ",n)
        play=False

    else:
        print("Try again")