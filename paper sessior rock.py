import random

def play_game():
    # Get the user's choice
    user_choice = input("Choose rock (r), paper (p), or scissors (s): ").lower()

    # Get the computer's choice
    computer_choice = random.choice(['r', 'p', 's'])

    # Determine the winner
    if user_choice == computer_choice:
        print(f"It's a tie! You both chose {user_choice}.")
        return 'tie'
    elif (user_choice == 'r' and computer_choice == 's') or \
         (user_choice == 'p' and computer_choice == 'r') or \
         (user_choice == 's' and computer_choice == 'p'):
        print(f"You win! You chose {user_choice} and the computer chose {computer_choice}.")
        return 'win'
    else:
        print(f"You lose. You chose {user_choice} and the computer chose {computer_choice}.")
        return 'lose'

# Play the game and keep track of the scores
user_wins = 0
computer_wins = 0
ties = 0

while True:
    result = play_game()
    if result == 'win':
        user_wins += 1
    elif result == 'lose':
        computer_wins += 1
    else:
        ties += 1

    play_again = input("Do you want to play again? (y/n) ").lower()
    if play_again != 'y':
        break

print(f"Final score: You won {user_wins} times, the computer won {computer_wins} times, and there were {ties} ties.")