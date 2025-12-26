import random

easy = ["apple","train","tiger","money","india"]
medium = ["python","bottle","monkey","laptop"]
hard = ["elephant","diamond","umbrella","continue"]

def play_game():
    print("welcome to the guessing game")
    print("choose difficulty(Easy,Medium,Hard)or Exit")

    #for choosing the deficulty
    entry = input("Enter your choise").lower()

    if entry == "exit":
        return True
    
    if entry == "easy":
        word = random.choice(easy)
    
    elif entry == "medium":
        word = random.choice(medium)

    elif entry == "hard":
        word = random.choice(hard)

    else:
        print("Invalid entry,try easy")
        word = random.choice(easy)

    print("now its time to guess the word...")
    attempt = 0

    #Game loop
    while True :
        guess = input("Enter your guess :").lower()

        if guess == "exit":
            print("thank you,you are out of the game")
            break

        attempt += 1
        if guess == word:
            print("congratulation ,you are guessed the word in",attempt,"attempt")
            print("Great!")
            break

        #for giving hint we are using trying to print
        hint = ""

        for i in range (len(word)):
            if guess[i] == word[i]:
                hint += guess[i]

            else :
                hint +="_"
        print("you are almost close ,hint :",hint)
    print("game over")
    return False

name = input("Enter your name:")
while True:
    game = play_game()

    if game:
        break
    a = input("Hey do you want to play a game (Yes/No):")

    if a == "No":
        print("Thank you,Goodbye")
        break           

