class Customer:
    bank_name = 'SBI'
    min_bal = 10000
    def __init__(self):
        self.name = None
        self.amount = None
        self.acc_no = None
        #self.w_amount = None

    def read(self):
        while True:
            self.name = input('Enter Customer name: ')
            self.amount = float(input('Enter Customer amount: '))
            self.acc_no = input('Enter Customer account number: ')
            #self.w_amount = float(input('Enter withdrawal amount: '))
            print()
            self.print()
            # if self.amount < Customer.min_bal:
            #   print(f'Sorry Insufficient balance')
            # elif self.amount < self.w_amount:
            #     print(f'Sorry Insufficient balance, pls check your account balance!!!')
            # else:
            #   self.amount = self.amount - self.w_amount
            #   print(f'Customer Bank name: {Customer.bank_name}')
            #   print(f'Customer name: {self.name}')
            #   print(f'Available balance: {self.amount}')
            #   print(f'Customer account number: {self.acc_no}')
            #   print()
            cm = input(f'Do you want to continue yes/no? ')
            if cm.lower() == 'no':
                print(f'Thank you for using')
                print(f'Visit Again...!!!')
                print()
                break
    def print(self):
        print(f'Customer Bank name: {Customer.bank_name}')
        print(f'Customer name: {self.name}')
        print(f'Available balance: {self.amount}')
        print(f'Customer account number: {self.acc_no}')

class Withdrawal(Customer):
    def __init__(self):
        super().__init__()
        self.w_amount = None
    def withdraw(self):
        #super().print()
        while True:
            self.w_amount = float(input('Enter withdrawal amount: '))
            if self.amount < Customer.min_bal:
              print(f'Sorry Insufficient balance')
            elif self.amount < self.w_amount:
                print(f'Sorry Insufficient balance, pls check your account balance!!!')
            else:
              self.amount = self.amount - self.w_amount
              print(f'Customer Bank name: {Customer.bank_name}')
              print(f'Customer name: {self.name}')
              print(f'Available balance: {self.amount}')
              print(f'Customer account number: {self.acc_no}')
              print()
            cm = input(f'Do you want to continue yes/no? ')
            if cm.lower() == 'no':
                print(f'Thank you for using')
                print(f'Visit Again...!!!')
                print()
                break

class Deposit(Customer):
    def __init__(self):
        super().__init__()
        self.d_amount = None

    def deposit(self):
        #super().read.self.amount
        while True:
            try:
                self.d_amount = float(input('Enter Deposit amount: '))
                self.amount += self.d_amount
                print(f'Customer Bank name: {Customer.bank_name}')
                print(f'Customer name: {self.name}')
                print(f'Available balance: {self.amount}')
                print(f'Customer account number: {self.acc_no}')
            except ValueError:
                print(f'Invalid amount, please try again...')

            cn = input(f'Do you want to continue yes/no? ')
            print()
            if cn.lower() == 'no':
                  print(f'Thank you for using')
                  print(f'Visit Again...!!!')
                  break

print(f'Welcome To {Customer.bank_name}')
w1 = Withdrawal()
w1.read()
w1.withdraw()
d1 = Deposit()
d1.deposit()
# c1.print()
#c1.withdraw()
#c1.deposit()
# c2 = Customer()
# c2.read()
# #c2.print()
# c2.withdraw()
# c2.deposit()

