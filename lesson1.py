

# 
# class Car:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color
# 
#     def info(self):
#         print(f"Машина {self.brand}, цвета {self.color}")
# 
#     def stop(self):
#         print(f"{self.brand} остановилась!")
# 
# car1 = Car("BMW", 'red')
# print(car1)
# print(car1.brand)
# print(car1.color)
# print(car1.info())
# print(car1.stop())

# class Animal:
#     def speak(self):
#         print("Животное издает звук")
# 
# class Dog(Animal):
#     def speak(self):
#         print("Gav Gav")
# 
# dog = Dog()
# dog.speak()

# class User:
#     def __init__(self, username):
#         self.username = username

#     def get_role(self):
#         return "User"

# class Admin(User):
#     def get_role(self):
#         return "Admin"

# user1 = User("Bob")
# admin1 = Admin("superuser")

# print(user1.get_role())
# print(admin1.get_role())



from datetime import datetime, timedelta


class Subscription:
    def __init__(self, name : str, price : float, duration_days : int):
        self.name = name 
        self.price = price
        self.duration_days = duration_days
        self.start_date = None
        self.end_date = None

    def activate(self):
        self.start_date = datetime.now()
        self.end_date = self.start_date + timedelta(days=self.duration_days)

    def is_active(self) -> bool:
        if not self.end_date:
            return False
        return datetime.now() < self.end_date

class User:
    def __init__(self, username : str):
        self.username = username
        self.balance = 0.0
        self.is_blocked = False
        self.subscription : Subscription | None = None
        self.history = []

    def deposit(self, amout : float):
        if amout <= 0:
            raise ValueError("Сумма должно быть положительной!")

        self.balance += amout
        print(f"added balance {amout}")

    def buy_subscription(self, subscription : Subscription):
        if self.is_blocked:
            print("Пользователь заблокирован!")

        if self.subscription and self.subscription.is_active():
            print("У вас уже имеет подписка!")

        if self.balance < subscription.price:
            print("Недостаточно средст!")

        self.balance -= subscription.price
        subscription.activate()
        self.subscription = subscription
        print(f"Куплена подписка {subscription.name}")

        self._chack_balance

    def _chack_balance(self):
        if self.balance < 0:
            self.is_blocked = True
            print("Автоблокировка из-за отрицательного баланса!")

    def get_info(self):
        sub_status = (
            self.subscription.name 
            if self.subscription and self.subscription.is_active()
            else "Нет автивной подписки"
        )

        return {
            "username": self.username,
            "balance": self.balance,
            "blocked": self.is_blocked,
            "subscription": sub_status
        }

class Admin(User):
    def block_user(self, user : User):
        user.is_blocked = True
        print("Пользователь заблокирован админом")

    def unblock_user(self, user : User):
        user.is_blocked = False
        print("Пользователь разблокирован админом")

    def change_balance(self, user : User, amount : float):
        user.balance += amount
        print(f"Админ пополнил баланс пользователя {amount}")

class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user : User):
        self.users.append(user)

    def get_user(self, username : str):
        return next((u for u in self.users if u.username == username), None)

    def list_user(self):
        return [user.get_info() for user in self.users]

manager = UserManager()

user1 = User("bob")
admin = Admin("ALice")

manager.add_user(user1)
manager.add_user(admin)

user1.deposit(300)

premium = Subscription("Premium", 200, 30)

user1.buy_subscription(premium)

