import random

def roll_dice():
    return random.randint(1, 6)

def play_game():
    print("Welcome to the Dice Rolling Game!")

while True:
    choice = input("Rolling Dice? (yes/no): ").lower()
    if choice == 'yes':
        result = roll_dice()
        print(f"You rolled a {result}!")
    elif choice== 'no':
        print("Thanks for playing! Goodbye!")
        break
    else:
        print("Invaled input. Please type 'yes' or 'no'.")

if __name__== "__main__": play_game()