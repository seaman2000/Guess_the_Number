import random

computer_number = 0
max_number = 0
counter = 0
troll_counter = 0
games_counter = 1

player_guesses = []

min_size = float('inf')

is_guessed = False
is_invalid = False
difficulty_chosen = False
showing_guess_number = True

closest_number = None

while True:
    is_invalid = False
    player_number = None

    if not difficulty_chosen:  # choose difficulty
        difficulty = input("Choose difficulty between Easy, Medium or Hard: ").strip().lower()

        if difficulty == "easy":
            max_number = 20
        elif difficulty == "medium":
            max_number = 50
        elif difficulty == "hard":
            max_number = 100
        else:
            print("Invalid difficulty. Please, choose between Easy, Medium or Hard.")
            continue

        troll_counter = 0
        computer_number = random.randint(1, max_number)
        difficulty_chosen = True

    player_input = input(f"Guess the number (1-{max_number}): ").strip()

    if not player_input.isdigit():
        print("Invalid input. Try again...")
        is_invalid = True
    else:
        player_number = int(player_input)
        if not player_number in range(1, max_number + 1):
            print(f"Please type a number which is between (1-{max_number})")
            is_invalid = True

    if is_invalid:
        troll_counter += 1
        if troll_counter == 3:
            print("You're joking...")
            showing_guess_number = False
            break
        continue

    counter += 1
    player_guesses.append(player_number)

    if player_number == computer_number:
        print("You guessed it!")
        is_guessed = True
        break
    elif player_number > computer_number:
        print("Too high!")
    else:
        print("Too low!")

    if counter >= 5:
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

        answer = input("Y or N ").strip().upper()

        while answer != "Y" and answer != "N":
            answer = input("I said Y or N!!!").strip().upper()

        if answer == "Y":
            closest_number = None
            player_guesses = []
            counter = 0
            min_size = float('inf')
            difficulty_chosen = False

            if games_counter >= 3:
                print("I am too tired for this, I need a break.")
                showing_guess_number = False
                break

            games_counter += 1
            continue
        else:
            break

if not is_guessed and showing_guess_number:
    print(f"The number to guess was: {computer_number}")


