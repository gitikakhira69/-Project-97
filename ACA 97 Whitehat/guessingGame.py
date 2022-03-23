import random
print ("GUESS THE NUMBER GAME")
number = random.randint(1,9)

#intializing
chances = 0

print("Guess The Number Between 1-9")

while chances < 5:
    guess = int(input("Enter Your Guess : "))

    if guess == number:
        print("Your Guess Is Correct CONGRATULATIONS YOU WON!!")

    elif guess < number :
        print("Your Guess Was Closer")
    else:
        print("Your Guess Was Too High")
    chances+=1

if not chances < 5:
    print("YOU LOSE!!The number is :",number)