# Problem:
#     File mein products likho
#     Cursor move karke dobara read karo

# f = open("try1.txt", "w+")
# f.write("Laptop\nMobile\nTablet")
# f.seek(0)
# print(f.read())
# f.close

# with open("try2.txt" , "w+") as f:
#     f.wri()
#     f.seek(0)
#     print(f.read())




# # Problem:
# #     Ek User class banao
# #     name, email constructor se
# #     display method

# class user:
#     def __init__(self ,name ,email):
#         self.name = name
#         self.email = email
    
#     def show(self):
#         print(self.name)
#         print(self.email)

# name = input("enter your name : ")
# email = input("enter your email : ")

# obj1 = user(name,email)
# obj1.show()


# hr = 23 
# print(hr)


# Problem:
    # File read karo, agar file na mile toh graceful message do

# try: 
#     with open("try1.txt" , "r") as f:
#         print(f.read())

# except: