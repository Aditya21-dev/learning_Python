# Q5. (Comprehension + Lambda + Logic)
# Problem:
#     Sirf even squares chahiye

# l1 = [1,2,3,4,5,6,7,8,9,0]

# result = [ x*x for x in l1 if x%2 == 0]
# print(result)


# recursion

def selfcallfunc(n):
    if n > 10:        # base condition
        return
    print(n)
    selfcallfunc(n + 1)

selfcallfunc(1)