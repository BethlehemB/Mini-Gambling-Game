import random

MAX_BET = 1000000
MIN_BET = 1



def roll_dice():
    dice_drawing = {
    1: (
            "-----",
            "|   |",
            "| o |",
            "|   |",
            "-----",
        ),
    2: (
            "-----",
            "|o  |",
            "|   |",
            "|  o|",
            "-----",
        ),
    3: (
            "-----",
            "|o  |",
            "| o |",
            "|  o|",
            "-----",
        ),
    4: (
            "-----",
            "|o o|",
            "|   |",
            "|o o|",
            "-----",
        ),
    5: (
            "-----",
            "|o o|",
            "| o |",
            "|o o|",
            "-----",
        ),
    6: (
            "-----",
            "|o o|",
            "|o o|",
            "|o o|",
            "-----",
        ),

    }
    
    dice = random.randint(1,6)
    print("You rolled: ", dice,"!")
    print("\n".join(dice_drawing[dice]))

    return dice





def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        print()
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number.")
    return amount





def get_guess():
    while True:
        guess = input("Guess what the dice will roll (1-6): ")
        if guess.isdigit():
            guess = int(guess)
            if guess <= 6 and guess >= 1:
                break
            else:
                print("Enter a valid number (1-6): ")
        else:
            print("Please enter a number.")
    return guess





def final_guess():
    while True:
        print()
        guess = input("REMINDER: this sum guess can be different from the sum of your guessed individual dices \nGuess what the sum of the two dice will be (2-12) ")
        if guess.isdigit():
            guess = int(guess)
            if guess <= 12 and guess >= 2:
                break
            else:
                print("Enter a valid number (2-12): ")
        else:
            print("Please enter a number.")
    return guess
    




def get_bet():
    while True:
        bet = input("\nWhat would you like to bet on each individual dice? $")
        print()
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return bet





def final_sum_bet(balance, dice_bet):
    print("REMINDER: if your sum is only off by two you recieve triple your bet\n")
    print(f"Your current balance after waging ${dice_bet} on each individual dice is ${balance - (dice_bet*2)}\n")
    new_bet = input(f"Would you like your bet for the sum to be the same as the bet for the individual dices ${dice_bet} or would you like to bet differently (I sugggest go big or go home): ")
    if new_bet.isdigit():
        new_bet = int(new_bet)
        if 0 <= new_bet <= MAX_BET:
            return new_bet
        else:
            print(f"Amount must be between $0 - ${MAX_BET}.")
    else:
        print("Please enter a number.")
    print()
    return new_bet





def guess_correct(name_roll, guessed_num, actual_num, balance, bet):
    if actual_num - 1 <= guessed_num <= actual_num + 1:
        print("Congratulations! Your guess on",name_roll, "was only off by one so you will get your bet back\n")
        balance = balance + bet
        print("Your new balance is: ", balance)
        print()
    elif actual_num == guessed_num:
        print("Congratulations! Your guess on ",name_roll, "was correct or was only off by one so you will be getting double your bet!\n")
        balance = balance + (bet * 2)
        print("Your new balance is: ", balance)
        print()
    else:
        print("Sorry your guess on", name_roll, "was incorrect and you loose $",bet)
        print()
        balance = balance - bet
        print("Your new balance is: ", balance)
        print()
    return balance





def correct_sum(guessed_sum, actual_sum, balance, bet):
    if actual_sum == guessed_sum or actual_sum - 2 <= guessed_sum <= actual_sum + 2:
        print("Congratulations! Your guessed sum was either correct or off by two! Your will get triple your bet\n")
        balance = balance + (bet * 3)
        print("Your new balance is: ", balance)
        print()
    elif actual_sum - 3 <= guessed_sum <= actual_sum + 3:
        print("Congratulations! Your guessed sum was only off by three so you will recieve your bet back\n")
        balance = balance + bet
        print("Your new balance is: ", balance)
        print()
    else:
        print("Sorry! Your guessed sum was incorrect and not within range to win anything. You lose your bet\n")
        balance = balance - bet
        print("Your new balance is: ", balance)
        print()
    return balance







def main():
    print("********************************************** WELCOME! **********************************************")
    name = input("                                     May I get your name: ")
    print(f"\nHello {name}, in this game you must ... and guess the sum the sum of these two rolls. \n")
    print("For the individual dice guesses, if you are off by one the amount you bet on will be returned to you. If your guess is correct you will get double your bet!")
    print("\nFor the sum guess, if you are off by three you will get your bet back and if you guess the sum correctly or are only off by two you will get triple your bet!\n")


    balance = deposit()
    name_roll1 = "Dice 1"
    name_roll2 = "Dice 2"
    answer = input("Would you like to play now? (yes/no): ")
    print()

    while answer.lower() != "Yes".lower() and answer.lower() != "No".lower():
        answer = input("\nPlease enter a valid response: \nWould you like to play now? (yes/no): ")
    
    if answer.lower() == "No".lower():
        print("Have a great day then!")
        return 0

    while answer.lower() == "Yes".lower():
        dice1 = get_guess()
        dice2 = get_guess()
        sum = final_guess()

        while True:
            bet = get_bet()
            sum_bet = int(final_sum_bet(balance,bet))
            total_bet = bet * 2 + sum_bet

            if total_bet > balance:
                print(f"\nYou do not have enough funds, your current balance is ${balance}")
            else:
                break
        print(f"You are betting ${bet} on each of your three guesses. Total bet is equal to: ${total_bet}")

        dice_num = roll_dice()
        dice_num2 = roll_dice()
        fsum = dice_num + dice_num2

        new_balance = guess_correct(name_roll1, dice1, dice_num, balance, bet)
        new_balance2 = guess_correct(name_roll2, dice2, dice_num2, new_balance, bet)
        final_balance = correct_sum(sum, fsum, new_balance2, sum_bet)

        if fsum == 7 or fsum == 12:
            print("JACKPOT!!! You rolled a snake eye (your sum was either a 7 or 12) which is considered rare")
            print("Not only will you get your sum bet back but you've won $2,000,000")
            final_balance = sum_bet + 2000000
            print(f"Your current balance is now ${final_balance}")
        
        if final_balance <= 0:
            print(f"Sorry! Your current balance is ${final_balance} get ya money up to play again")
            return 0
        
        answer = input("Play again? (yes/no) ")

            


main()