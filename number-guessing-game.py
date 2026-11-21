import random


def choose_difficulty():
    print("Choose a difficulty:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-500)")

    while True:
        choice = input("Enter 1, 2, or 3: ").strip()
        if choice == "1":
            return 50
        if choice == "2":
            return 100
        if choice == "3":
            return 500
        print("Please enter a valid difficulty.")


def play_round(maximum):
    number_to_guess = random.randint(1, maximum)
    attempts = 0

    print(f"I'm thinking of a number between 1 and {maximum}.")

    while True:
        try:
            guess = int(input("Make a guess: "))
            attempts += 1

            if guess < 1 or guess > maximum:
                print(f"Please guess a number from 1 to {maximum}.")
                continue

            if guess < number_to_guess:
                print("Too low.")
            elif guess > number_to_guess:
                print("Too high.")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                return attempts
        except (ValueError, EOFError):
            print("Please enter a valid integer.")


def main():
    print("Welcome to the Number Guessing Game!")
    best_attempts = None

    while True:
        maximum = choose_difficulty()
        attempts = play_round(maximum)

        if best_attempts is None or attempts < best_attempts:
            best_attempts = attempts
            print(f"New best score: {attempts} attempts.")
        else:
            print(f"Best score: {best_attempts} attempts.")

        replay = input("Play again? (y/n): ").strip().lower()
        if replay not in ("y", "yes"):
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()