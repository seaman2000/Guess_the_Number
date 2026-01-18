import random

computer_number = random.randint(1, 100)
counter = 0
games_counter = 1
player_guesses = []
min_size = float('inf')
is_guessed = False
closest_number = None

while True:
    player_input = input("Guess the number (1-100): ")
    if not player_input.isdigit():
        print("Invalid input. Try again...")
        continue
    counter += 1
    player_number = int(player_input)
    if player_number == computer_number:
        print("You guessed it!")
        is_guessed = True
        break
    elif player_number > computer_number:
        print("Too high!")
    else:
        print("Too low!")
    player_guesses.append(player_number)
    if counter == 5:
        print("You don't have any more tries left.")
        for each_integer in player_guesses:
            difference = abs(each_integer - computer_number)
            if difference < min_size:
                min_size = difference
                closest_number = each_integer
        if min_size <= 5:
            print("You were so close though!")
            print(f"From your guessed numbers, the closest was {closest_number}, "
                  f"{min_size} numbers away from the target.")
        print("Do you want to play again?")
        answer = input("Y or N")
        answer = answer.strip().upper()
        if answer == "Y":
            closest_number = None
            player_guesses = []
            counter = 0
            min_size = float('inf')
            computer_number = random.randint(1, 100)
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
if not is_guessed:
    print(f"The number to guess was: {computer_number}")

