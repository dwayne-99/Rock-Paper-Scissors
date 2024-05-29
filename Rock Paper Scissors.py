import random

user_choice = input("Enter a choice (rock, paper, scissors) ")
computer_choice = random.choice(["rock", "paper", "scissors"])

if user_choice == computer_choice:
  print(f"It's a tie! The computer chose {computer_choice}")
elif user_choice == "rock" and computer_choice == "scissors":
  print(f"You win! The computer chose {computer_choice}")
elif user_choice == "paper" and computer_choice == "rock":
  print(f"You win! THe computer chose {computer_choice}")
elif user_choice == "scissors" and computer_choice == "paper":
  print(f"You win! The computer chose {computer_choice}")
else:
  print(f"You lose! The computer chose {computer_choice}")