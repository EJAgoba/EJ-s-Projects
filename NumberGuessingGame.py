import random

guessing_range = []
for _ in range(101):
    guessing_range.append(_)


def actual_game():
    #Get computer to choose a random number from guessing range
    random_number = random.choice(guessing_range)

    print("Welcome to the guessing game")
    difficulty_level = input("I have a number from 1 - 100. Guess it; Do you want to play the easy or hard version? 'E' for easy, 'H' for hard: ").lower()
    def tries():
        """This function lets me pick the right amount of tries based on user's chosen difficulty level"""
        if difficulty_level == 'e':
            return 10
        elif difficulty_level == 'h':
            return 5
    no_tries = tries()
    game_over = False
    while no_tries > 0 and game_over == False:
        print(f"You have {no_tries} guesses remaining to guess the correct number") 
        users_guess = int(input("Guess a number: "))
        if users_guess == random_number:
            game_over = True
            print("Game over! You were right on!")
        elif users_guess > random_number:
            print("Too high")
            no_tries = no_tries - 1
        elif users_guess < random_number:
            print("Too low")
            no_tries = no_tries - 1
        if no_tries == 0:
            print(f"Out of guesses! Game over. The number was {random_number}")
            game_over = True

actual_game()
play_again = input("Do you want to play again? Y or N?").lower()
if play_again == 'y':
    actual_game()
elif play_again == 'n':
    print("Aight bet! Game over!")
    
    

    
