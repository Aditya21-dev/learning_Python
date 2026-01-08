# def num_n(n):
#     print(n)
#     if n == 0:
#         return "complited"
#     return num_n(n-1)

# print(num_n(10))


# def num_n(n):
#     if n == 0:
#         return n 
#     return n + num_n(n-1)

# print(num_n(50))


# def num_p(n):
#     if n == 1:
#         return 1
#     return n*num_p(n-1)

# print(num_p(5))

# def revs_S(s):
#     if s == "":
#         return s
#     return revs_S(s[1:]) + s[0]

# print(revs_S("Aditya"))




def fibo(n):
    if n == 0 or  n == 1:
        return n
    # print(n)
    return fibo(n-1)+ fibo(n-2)

print(fibo(6))