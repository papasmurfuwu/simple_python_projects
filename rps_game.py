import random 

# Rock paper scissors game in terminal 
# while loop for game --> check if continue playing, show wins and losses if end + end message 
#   set win conditions 
#   set random select rock/ paper/ scissors

# win cases:
# rock --> scissors
# paper --> rock 
# scissors --> paper        


win_or_lose = str
wins_no = losses_no = 0 

# Defining game logic function 
def win_cases(user_input):
    global wins_no, losses_no
    choices_dict = {1: "rock",
                    2: "paper",
                    3: "scissors"}
    bot_choice = random.randint(1, 3)
    
    # Check for win cases 
    if (user_input == "rock" and bot_choice == 3) or (user_input == "paper" and bot_choice == 1) or (user_input == "scissors" and bot_choice == 2): 
        win_or_lose = f"\nYou have won! Bot has chosen {choices_dict[bot_choice]}."
        wins_no += 1 

    elif choices_dict.get(user_input) == bot_choice:
        win_or_lose = "\nA tie!"

    else: 
        win_or_lose = f"\nYou have lost... Bot has chosen {choices_dict[bot_choice]}."
        losses_no += 1
    
    return win_or_lose, wins_no, losses_no

play_again = "y" 


print("Welcome to Rock Paper Scissors! Please enter your first choice!")
while play_again == "y": 
    user_input = input("Type here: ").strip().lower()
    win_or_lose, wins_no, losses_no = win_cases(user_input)
    
    print(win_or_lose)
    print(f"You currently have {wins_no} wins and {losses_no} losses.")
    play_again = input("Would you like to play another round? (y/n): ")
    if play_again == 'y':
        continue 
    else: 
        print("\nThank you for playing, and see you next time!")
