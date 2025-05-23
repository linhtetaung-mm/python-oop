

class BankAccount:
    MIN_BALANCE = 100

    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if self._is_valid_amount(amount):
            self._balance += amount
            print(self.__log_transaction("deposit", amount))
        else:
            print("Deposit amount must be positive number")
    
    def show_info(self):
        print(f"Owner: {self.owner}, Balance: {self._balance}")

    def _is_valid_amount(self, amount):
        return amount > 0
    
    def __log_transaction(self, transaction_type, amount):
        return f"Logging {transaction_type} of ${amount}.\nNew balance: ${self._balance}."
    
    @staticmethod
    def is_valid_interest_rate(rate):
        return 0<= rate <= 5


def main():
    account = BankAccount("John Snow", 300)
    account.deposit(30)
    print(BankAccount.is_valid_interest_rate(3))
    print(BankAccount.is_valid_interest_rate(7))
    print(account._is_valid_amount(20))
    # print(account.__log_transaction("deposit", 200))



if __name__ == "__main__":
    main()
