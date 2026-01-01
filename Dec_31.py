# Q2. (Multiple Inheritance + MRO Trap)
#     Problem:
#     Output predict karo (most asked)
class a:
    def show(self):
        print("a")
class b(a):
    def show(self):
        print("b")
class c:
    def show(self):
        print("c")
class d(b, c):
    pass

obj1 = d()
obj1.show()

''' MRO :- method resoluton order
           iska matlab ye hota hai ki python kis order mein class k methods ko dhundna start karega.
           isliliye pahle b pe gya mill gya show function toh b return kar diya..! '''





# Q3. (Abstract Class + Payment System)
# Problem:
    # Payment system banao jisme:
    # abstract method pay()
    # subclasses: UPI, Card
    
from abc import ABC, abstractmethod

class payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class UPI(payment):
    def pay(self,amount):
        print(f'Paid {amount} via UPI')

class card(payment):
    def pay(self,amount):
        print(f'Paid {amount} via card')


transaction1 = card()
transaction1.pay(45000) 






# Q4. (Encapsulation + Access Specifier)
    # Problem:
    #     Account balance ko secure karo

class Account:
    __balance = 0
    def __init__(self, balance):
        self.__balance = balance  # private

    def get_balance(self):
        return self.__balance
    
acc = Account(5000)
print(acc.get_balance())
