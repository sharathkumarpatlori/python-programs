import random

def play_round(player, number_to_guess):
    guess = int(input(f"{player}, guess a number between 1 and 10: "))
    if guess == number_to_guess:
        print("Correct! You earn 10 points.")
        return 10
    else:
        print(f"Wrong! The number was {number_to_guess}.")
        return 0

def main():
    print("Welcome to Guess the Number Game!")
    player = input("Enter your name: ")
    score = 0
    rounds = 3

    for _ in range(rounds):
        number_to_guess = random.randint(1, 10)
        score += play_round(player, number_to_guess)

    print(f"Game over. {player}'s total score: {score}")

if __name__ == "__main__":
    main()