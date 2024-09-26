import sys
class Customer:
    bank_name = 'HDFC'
    min_balance = 10000
    def __init__(self, name, balance = 0.0):
        self.name = name
        self.balance = balance

    def deposit(self, amt):
        self.balance = self.balance + amt
        #print(f'Customer name: {c1.name}')
        print(f'Account balance: {self.balance}')
    def withdraw(self, amt):
        if amt > self.balance:
            print('Insufficient funds, cat not perform operation!!!')
            sys.exit()
        elif Customer.min_balance > self.balance:
            print('Minimum balance!!!')
            sys.exit()
        self.balance = self.balance - amt
        #print(f'Customer name: {self.name}')
        print(f'Account balance: {self.balance}')


print(f'Welcome to {Customer.bank_name} Bank')
name = input('Enter your name: ')
c1 = Customer(name)
while True:
    print(f'd-deposit \nw-withdrawal \ne-exit')
    option = input('Choose your option: ')
    if option == 'd' or option == 'D':
        amt = float(input('Enter deposit amount: '))
        c1.deposit(amt)
    elif option == 'w' or option == 'W':
        amt = float(input('Enter withdrawal amount: '))
        c1.withdraw(amt)
    elif option == 'e' or option == 'E':
        print('Thank you for Banking')
        print(f'Visit Again!!!')
        sys.exit()
    else:
        print('Invalid option, please try again')

