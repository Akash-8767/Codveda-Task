import random

def random_guessing_game():
    number_for_guess_to_user = random.randint(1, 100)     
    maximum_attempt = 15

    print(" Welcome in the Random Number Guessing Gmame !!!")
    print("You have the same number which i guess , Rang of number be 1 to 100.")
    print("You have 15 attempts to guess the correct number.\n")

    for attempt in range(1, maximum_attempt + 1):
        try:
            guess = int(input(f"Enter the number that you guess: "))
        except ValueError:
            print("Check The input value, it not be negative \n")
            continue

        if guess < 1 or guess > 100:
            print(" Your guess is out of range.\n")
            continue

        if guess < number_for_guess_to_user:
            print("Opps, You Guess The Too Low Number")
        elif guess > number_for_guess_to_user:
            print("Opps, You Guess The Too High Number")
        else:
            print(" Wow You guessed the correct number!")
            print(" !!! WINNER !!!")
            break
    else:
        print(" Sorry, you've used all your attempts.")
        print(f"The number was: {number_to_guess_user}")
        print(" !!! GAME OVER !!!")


random_guessing_game()



