# from abc import ABC, abstractmethod

# class Payment(ABC):
#     @abstractmethod
#     def pay(self, amount):
#         pass
    
# class CardPayment(Payment):
#     def pay(self, amount):
#         print("Card payment", {amount})
        
# class CryptoPayment(Payment):
#     def pay(self, amount):
#         print("Cash payment", {amount})
        
# def result(payment : Payment):
#     payment.pay(1000)
 
 
# result(CryptoPayment())   
# result(CardPayment())




class A:
    def hello(self):
        print("A")

class B(A):
    def hello(self):
        print("B")

class C(A):
    def hello(self):
        print("C")
        
class D(B, C):
    pass

d = D()
d.hello()
print(D.__mro__)