import random
def get_choices():
    player_choice = input("Enter a choice: ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices_dict = {"player": player_choice, "computer": computer_choice}
    return choices_dict

def check_win(player, computer):
    print(f"You chose {player}. Computer chose {computer}.")
    if player == computer:
        return "Tie." 
    elif player == "rock":
        if computer == "scissors":
            return "Rock beats scissors. You win!"
        elif computer == "paper":
            return "Paper beats rock. You lose."
    elif player == "paper":
        if computer == "scissors":
            return "Scissors beats paper. You lose."
        elif computer == "rock":
            return "Paper beats rock. You win!"
    elif player == "scissors":
        if computer == "rock":
            return "Rock beats scissors. You lose."
        elif computer == "paper":
            return "Scissors beats paper. You win!"

choices = get_choices()
result = check_win(choices["player"],choices["computer"])
print(result)
print("Thank you for playing.")