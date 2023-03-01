#My first portfolio project
#Bank Account

import random
#Maximum amounts for any transaction
MAX_DEPOSIT = 1000.00
MAX_WITHDRAW = 1000.00
MAX_TRANSFER = 1000.00


class Bank_Account():
    account_name = " "
    account_ID = 0
    checking_balance = float(0)
    saving_balance = float(0)

    def __init__(self) -> None:
        self.account_name = input("What is your name? ")
        self.checking_balance = float(input("What is your current balance? "))
        self.account_ID = self.account_name.upper() + " " + str(random.randint(0, 1000))
        self.saving_balance = 0.0
        return
    
    def checkAccount(self):
        print(f"Account ID:{self.account_ID}\nName for the account: {self.account_name}\nBalance: {self.checking_balance}")
    
 #Withdraw method
    def withdraw(self):
        print(f"Your balance is {self.checking_balance}")
        question = float(input(f"Hi {self.account_name}, how much would you like to withdraw?"))
        if type(question) is not float:
            print("You must enter a valid number.")
        elif question > self.checking_balance:
            print("You cannot withdraw that amount.")
        elif question > MAX_WITHDRAW:
            print("You have exceeded the limit of which you could withdraw at once.") 
        else:
            self.checking_balance -= question
        print("Your new balance is " + str(self.checking_balance))

#Deposit method
    def deposit(self):
        answer = input(f"Hi {self.account_name}, would you like to see your current balance? Y or N\n")
        if type(answer) is not str:
            print("You must type Y(es) or N(o) please.")
        elif answer == 'Y' or 'y':
            print("Your balance is " + str(self.checking_balance))
        else:
            print()

        answer2 = float(input("How much money would you like to deposit into your account?"))
        if type(answer2) is not float:
            print("You must enter a valid number.")
        elif answer2 > MAX_DEPOSIT:
            print("You have exceeded the limit of which you could deposit at once.")
        else:
            self.checking_balance += answer2
        print(f"Your new balance is " + str(self.checking_balance))
    
#transfer between Savings and Checking account
    def transfer(self):
        print(f"Your current balance in savings is {self.saving_balance} and your current balance in checkings is {self.checking_balance}.")
        answer = input("Which account will you be transferring money to?\n'S' for savings \n'C' for checking\n")
        
        if type(answer) is not str:
            print("Please input a valid option: ")
        elif answer == 'S' or 's':
            answer2 = float(input("How much would you like to transfer into your savings account?: "))
            if answer2 > self.checking_balance:
                print("You do not have enough to transfer!")
            else: 
                self.saving_balance += float(answer2)
                self.checking_balance -= float(answer2)
            print(f"Your new balance in your savings account is {self.saving_balance}.")
        elif answer == 'C' or 'c':
            answer2 = float(input("How much would you like to transfer into your checking account?: "))
            if answer2 > self.saving_balance:
                print("You do not have enough to transfer!")
            else: 
                self.checking_balance += float(answer2)
                self.saving_balance -= float(answer2)
            print(f"Your new balance in your savings account is {self.checking_balance}.")
        else:
            print("Choose valid option.")
        
        



def main():
    print("Welcome to our bank and thank you for banking with us!")
    user = Bank_Account()
    print(f"Your account ID is now {user.account_ID}")
    while True:
        answer = input("Press 1 to deposit: \nPress 2 to withdraw: \nPress 3 to transfer money: \nPress 'q' to quit: \n")
        if answer == '1':
            user.deposit()
        elif answer == '2':
            user.withdraw()
        elif answer == '3':
            user.transfer()
        elif answer == 'q':
            break
        else:
            print("Please enter valid option.")
        print("Thank you for banking with us!")
    
main()

