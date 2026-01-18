import random
from cmath import inf

computer_number = random.randint(1, 100)
counter = 0
games_counter = 0
player_guesses = []
min_size = inf
is_guessed = False
while True:
    counter += 1
    player_input = input("Guess the number (1-100): ")
    if not player_input.isdigit():
        print("Invalid input. Try again...")
        continue
    player_number = int(player_input)
    if player_number == computer_number:
        print("You guessed it!")
        is_guessed = True
        break
    elif player_number > computer_number:
        print("Too high!")
    else:
        print("Too low!")
    if counter == 5:
        print("You don't have any more tries left.")
        for each_string in player_guesses:
            each_integer = int(each_string)
            difference = abs(each_integer - computer_number)
            if difference < min_size:
                min_size = difference
        print("You were so close though!")
        print(f"From your guessed numbers, the closest of yours was {min_size} numbers from the target.")
        print("Do you want to try again?")
        answer = input("Y or N")
        if answer == "Y":
            if games_counter >= 3:
                print("I am too tired for this, I need a break.")
                break
            else:
                games_counter += 1
                continue
        elif answer == "N":
            break
        else:
            print("Invalid input, please choose between Y to continue and N to fail.")
    player_guesses += player_input

if not is_guessed:
    print(computer_number)

