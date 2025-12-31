# Q2. (Multiple Inheritance + MRO Trap)
#     Problem:
#     Output predict karo (most asked)
# class a:
#     def show(self):
#         print("a")
# class b(a):
#     def show(self):
#         print("b")
# class c:
#     def show(self):
#         print("c")
# class d(b, c):
#     pass

# obj1 = d()
# obj1.show()

# ''' MRO :- method resoluton order
#            iska matlab ye hota hai ki python kis order mein class k methods ko dhundna start karega.
#            isliliye pahle b pe gya mill gya show function toh b return kar diya..! '''






from abc import ABC, abstractclassmethod

class payment(ABC):
    @abstractclassmethod
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