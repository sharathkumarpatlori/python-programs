# guess_number_starter.py
import random

def play_round(player, number_to_guess, round_number):
    print(f"\nRound {round_number}:")
    # TODO: Ask the player to guess a number between 1 and 10
    # TODO: If guess is correct, print message and return 10 points
    # TODO: Else, print correct number and return 0 points

def main():
    print("Welcome to Guess the Number Game!\n")
    player = input("Enter your name: ")
    score = 0
    rounds = 3

    for i in range(1, rounds + 1):
        number_to_guess = random.randint(1, 10)
        # TODO: Call play_round and add the returned points to score

    # TODO: Print final score for player
    
if __name__ == "__main__":
    main()
