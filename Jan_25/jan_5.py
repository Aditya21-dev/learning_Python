from functools import reduce

# def dec(fx):
#     def odd(n):
#         for i in range(0,n+1,2):
#             print(i+1)        
#     return odd

# @dec
# def even(n):
#     for i in range(0,n+1,2):
#         print(i)
        
# n1 = int(input("enter nth term = "))
# even(n1)



# def print_1_to_10(n):
#     for i in range (0,n+1):
#         yield i

# ans = print_1_to_10(10)
# # print(list(ans))

# print(next(ans))
# print(next(ans))
# print(next(ans))



add = lambda a,b: a+b
# print(add(2,4))

li = [1,34,56,6,78]

print(list(map(lambda x:x*2,li)))

print(list(map(lambda x:x*2 if x%2==0 else 0,li)))

print(list)



nums = [1, 2,3,4,5,6]

print(reduce(lambda a, b: a + b, nums))
# print(result)