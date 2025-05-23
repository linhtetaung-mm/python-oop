
'''
How Encapsulation Works :

Data Hiding: The variables (attributes) are kept private or protected, 
meaning they are not accessible directly from outside the class. 
Instead, they can only be accessed or modified through the methods.

Access through Methods: Methods act as the interface 
through which external code interacts with the data stored in the variables. 
For instance, getters and setters are common methods used to retrieve and update the value of a private variable.

Control and Security: By encapsulating the variables and only allowing their manipulation via methods, 
the class can enforce rules on how the variables are accessed or modified, 
thus maintaining control and security over the data.
'''

#Bad Example without encapsulation
class BadBankAccount:
    def __init__(self, balance=0):
        self.balance = balance

#With encapsulation
class BankAccount:
    def __init__(self):
        self._balance = 0.0
    
    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        if not self._is_valid_amount(amount):
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount
    
    def withdraw(self, amount):
        if not self._is_valid_amount(amount):
            raise ValueError("Withdraw amount must be positive.")
        elif amount > self._balance:
            raise ValueError(f"Not enugh balance(Balance: {self._balance})")
        else:
            self._balance -= amount
    
    def _is_valid_amount(self, amount):
        return amount > 0


def main():
    #Bad Example
    bad_account = BadBankAccount(200)
    print("Balance:", bad_account.balance)
    bad_account.balance = -20
    print("Balance:", bad_account.balance)

    #With Encapsulation
    account = BankAccount()
    print("Balance:", account.balance)
    account.deposit(200)
    print("Balance:", account.balance)
    account.withdraw(150)
    print("Balance:", account.balance)

    # account.deposit(-20)
    # account.withdraw(-10)
    # account.withdraw(100)



if __name__ == "__main__":
    main()



