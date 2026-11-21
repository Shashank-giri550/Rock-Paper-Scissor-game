
import random

CHOICES = ["rock", "paper", "scissors"]


def get_player_choice():
    """Keep asking until the player enters a valid choice (case-insensitive)."""
    while True:
        choice = input("Enter Rock, Paper, or Scissors: ").strip().lower()
        if choice in CHOICES:
            return choice
        print("Invalid input! Valid options are: Rock, Paper, Scissors.")


def get_rounds():
    """Keep asking until the player enters a positive whole number."""
    while True:
        try:
            rounds = int(input("How many rounds do you want to play? (e.g. 3, 5): "))
        except ValueError:
            print("Please enter a whole number.")
            continue
        if rounds > 0:
            return rounds
        print("Number of rounds must be at least 1.")


def decide_winner(player, computer):
    """Return 'player', 'computer' or 'draw'."""
    if player == computer:
        return "draw"
    elif player == "rock" and computer == "scissors":
        return "player"
    elif player == "scissors" and computer == "paper":
        return "player"
    elif player == "paper" and computer == "rock":
        return "player"
    else:
        return "computer"


def main():
    print("=== Rock, Paper & Scissors ===")
    total_rounds = get_rounds()
    player_score = 0
    computer_score = 0

    for round_no in range(1, total_rounds + 1):
        print(f"\n--- Round {round_no} of {total_rounds} ---")
        player = get_player_choice()
        computer = random.choice(CHOICES)

        print(f"You chose: {player.capitalize()}")
        print(f"Computer chose: {computer.capitalize()}")

        result = decide_winner(player, computer)
        if result == "player":
            player_score += 1
            print("You win this round!")
        elif result == "computer":
            computer_score += 1
            print("Computer wins this round!")
        else:
            print("It's a draw!")

        print(f"Score -> You: {player_score} | Computer: {computer_score}")

    print("\n=== Game Over ===")
    print(f"Final Score - You: {player_score} | Computer: {computer_score}")
    if player_score > computer_score:
        print("You win the game!")
    elif computer_score > player_score:
        print("Computer wins the game!")
    else:
        print("The game is a draw!")


if __name__ == "__main__":
    main()