#My first portfolio project
#Ideas include: Tic Tac Toe, Interactive Basketball Game, Zombie Storyline, Calculator,Bank Account

class Bank_Account():
    account_name = " "
    account_ID = 0
    balance = float(0)

    def __init__(self, name, id, balance) -> None:
        self.account_ID = id
        self.account_name = name
        self.balance = balance
        return
    
    def displayAccount(self):
        return f"Account ID:{self.account_ID} Name for the account: {self.account_name} Balance: {self.balance}"

    def withdraw(self):
        new_balance = 0
        question = int(input(f"Hi {self.account_name}, how much would you like to withdraw?"))
        if type(question) is not int:
            print("You must input a valid number.")
        elif question > self.balance:
                print("You cannot withdraw that amount.")
        else:
            new_balance = self.balance - question
        print("Your new balance is " + str(new_balance))
    
class main():
    user1 = Bank_Account("James", 1, 500)
    user1.withdraw()

main()

