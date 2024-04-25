import random

def hand_cricket():
    print("Welcome to Hand Cricket!")

    while True:
        print("\nYou are batting.")
        player_score = 0

        while True:
            try:
                player_choice = int(input("Enter your number (1-6): "))
                if 1 <= player_choice <= 6:
                    break
                else:
                    print("Invalid input. Please enter a number between 1 and 6.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 6.")

        computer_choice = random.randint(1, 6)
        print(f"Computer's choice: {computer_choice}")

        if player_choice == computer_choice:
            print("Out! Your innings is over.")
            break
        else:
            player_score += player_choice
            print(f"Your score: {player_score}")

        print("\nComputer is batting.")
        computer_score = 0

        while True:
            computer_choice = random.randint(1, 6)
            print(f"Computer's choice: {computer_choice}")

            try:
                player_choice = int(input("Enter your number to bowl (1-6): "))
                if 1 <= player_choice <= 6:
                    break
                else:
                    print("Invalid input. Please enter a number between 1 and 6.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 6.")

        if player_choice == computer_choice:
            print("Out! Computer's innings is over.")
            break
        else:
            computer_score += computer_choice
            print(f"Computer's score: {computer_score}")

    print("\nGame Over!")
    print(f"Your final score: {player_score}")
    print(f"Computer's final score: {computer_score}")

    if player_score > computer_score:
        print("Congratulations! You win!")
    elif player_score < computer_score:
        print("Sorry, you lose. Better luck next time!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    hand_cricket()