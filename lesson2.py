# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance


# account = BankAccount(1000)
# account.balance == -100000

# class BankAccount:
#     def __init__(self, balance):
#         self._balance = balance
# 
#     def deposit(self, amount):
#         if amount == 0:
#             print("Сумма должно быть положительным!")
#         self._balance += amount
# 
#     def withdraw(self, amount):
#         if amount > self._balance:
#             print("Недостаточно средств")
#         self._balance -= amount
# 
#     def get_balance(self):
#         return self._balance
# 
# account = BankAccount(1000)
# account.withdraw(200)
# print(account.get_balance())


# class PaymentMethod:
#     def pay(self, amount):
#         raise NotImplementedError
# 
# class CardPayment(PaymentMethod):
#     def pay(self, amount):
#         return f"Оплата картой : {amount}"
# 
# class CryptoPayment(PaymentMethod):
#     def pay(self, amount):
#         return f"Оплата криптой : {amount}"
# 
# 
# def payment(payment_method : PaymentMethod, amount):
#     return payment_method.pay(amount)
# 
# print(payment(CardPayment(), 100))
# print(payment(CryptoPayment(), 200))


from __future__ import annotations


class BankAccount:
    bank_name = "StepBank"

    def __init__(self, owner : str, balance : int = 0):
        self.owner = owner
        self._history = []
        self.__balance = 0
        self.deposit(balance)

    @property
    def balance(self) -> int:
        return self.__balance

    @balance.setter
    def balance(self, value : int) -> None:
        if not isinstance(value, int):
            print("Баланс должен быть int")
        if value < 0:
            print("Баланс не может быть отриацтельным")
        self.__balance = value

    def deposit(self, amount: int) -> None:
        self.__validate_amount(amount)
        self.balance = self.balance + amount
        self._add_history(f"+{amount}")

    def withdraw(self, amount : int) -> None:
        self.__validate_amount(amount)
        if amount > self.balance:
            print("Недостаточно средст")
        self.balance = self.balance - amount
        self._add_history(f"-{amount}")
        
    def show_history(self) -> List[str]:
        return list(self._history)

    def _add_history(self, record : str) -> None:
        self._history.append(record)

    def __validate_amount(self, amount : int):
        if not isinstance(amount , int):
            print("Баланс должен быть int")
        if amount <= 0:
            print("Баланс не может быть отриацтельным")


class CashBackAccount(BankAccount):
    def deposit(self, amount : int):
        super().deposit(amount)
        cashback = amount // 100
        if cashback:
            self.balance = self.balance + cashback
            self._add_history(f"cashback +{cashback}")

acc = BankAccount("Bob", 1000)
acc.withdraw(200)
acc.deposit(50)
print(acc.owner)
print(acc.balance)
print(acc.show_history())

acc._add_history("Manual record (bad practice)")
print("History 2", acc.show_history())

# print(acc.__balance) - так нельзя делать

print("Hacked balance", acc._BankAccount__balance)

vip = CashBackAccount("VIP", 1000)
vip.deposit(500)
print("Vip History", vip.show_history())
print("Vip balance", vip.balance)