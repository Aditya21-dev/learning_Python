# def num_n(n):
#     print(n)
#     if n == 0:
#         return "complited"
#     return num_n(n-1)

# print(num_n(10))


def num_n(n):
    if n == 0:
        return n 
    return n + num_n(n-1)

print(num_n(50))