class BankAccount:
    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance

    @property
    def owner(self):
        return self.__owner
    
    @owner.setter
    def owner(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Invalide type")
        if not value:
            raise ValueError("Invalid value")
        self.__owner = value

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, value: float):
        if not isinstance(value, float):
            raise TypeError("Invalide type")
        if value < 0:
            raise ValueError("Invalid value")
        self.__balance = value

    def deposit_money(self, value: float):
        if value < 0:
            raise ValueError("Invalid value")
        self.balance += value
        print("Money added succesfully")

    def withdraw_money(self, value: float):
        if value > self.balance:
            raise ValueError("Invalid value")
        self.balance -= value
        print("Money withdrawed succesfully")

ba1 = BankAccount("James", 18000.0)
ba1.deposit_money(4300.0)
print(ba1.balance)
ba1.withdraw_money(14000.0)
print(ba1.balance)