import random

print("Welcome to Rock-Paper-Scissors Game!\n")
print("Instructions:")
print("- Type 'rock', 'paper', or 'scissors' to make your move.")
print("- Type 'quit' anytime to exit the game.\n")

choices = ['rock', 'paper', 'scissors']
user_score = 0
computer_score = 0
round_number = 1

while True:
    print(f"\n--- Round {round_number} ---")
    user_choice = input("Your move (rock/paper/scissors): ").lower()

    if user_choice == 'quit':
        print("\nThanks for playing!")
        break

    if user_choice not in choices:
        print("Invalid input! Please choose rock, paper, or scissors.")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Game Logic
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    # Show score
    print(f"Score => You: {user_score} | Computer: {computer_score}")
    round_number += 1

# Final Score Summary
print("\n--- Game Over ---")
print(f"Final Score => You: {user_score} | Computer: {computer_score}")
if user_score > computer_score:
    print("Congrats! You won the game.")
elif user_score < computer_score:
    print("You lost the game. Better luck next time!")
else:
    print("It's a tie game.")
