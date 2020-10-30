# bank account class
class BankAccount:
    def __init__(self, full_name, account_number, routing_number, balance):
        self.__full_name = full_name
        self.__account_number = account_number
        self.__routing_number =routing_number
        self.__balance = float(balance)
    # deposit function 
    def deposit(self,amount):
        self.__balance += amount
    # withdraw function
    def withdraw(self, amount):
        if (amount <= self.__balance):
            self.__balance -= amount
            print(f'Amount Withdrawn: {amount}')
        else:
            print('Insufficient funds.')
            self.__balance -= 10
    # balance function 
    def balance(self, full_name, balance):
        return print(f'Hi, {self.__full_name} Here is Your Balance: {self.__balance}')
    # interest function 
    def add_interest(self):
        interest = self.__balance *  0.00083
        self.__balance += interest
    #print receipt
    def print_receipt(self):
        print(self.__full_name)
        print(f'Account No.: ****{str(self.__account_number)[-4:]}')
        print(f'Routing No.: {self.__routing_number}')
        print(f'Balance: $' '{:.2f}'.format(self.__balance)) 
    #get users input for yes or  no prompts
    def get_user_input(self,prompt):
        user_input = str(input(prompt)).lower()
        print(user_input)
        if (user_input == 'yes' or user_input == 'y'):
            return True
        else:
            return False
    #withdraw from atm
    def atm_widthdraw(self):
        if self.get_user_input("would you like to Withdraw Money from the ATM? : Yes or No ? : "):
            if self.get_user_input("Do you want to check your balance?: Yes or No?"):
                print(self.__balance)
            withdraw_amount = float(input('How much do you want to withdraw?: '))
            self.withdraw(withdraw_amount)
            self.print_receipt()






user1 = BankAccount('Joshua', 101010101, 1010010100101, 500)
user1.deposit(500)
user1.withdraw(1000.01)
user1.add_interest()
user1.print_receipt()
user1.atm_widthdraw()
