# Q5. (Comprehension + Lambda + Logic)
# Problem:
    # Sirf even squares chahiye

l1 = [1,2,3,4,5,6,7,8,9,0]

result = [ x*x for x in l1 if x%2 == 0]
print(result)


# recursion

def count(n):
    if n == 0:
        return
    print(n)
    count(n-1)

count(5)





# Q7. (Exception Handling + Custom Error)
# Problem:
#     Age < 18 ho toh custom exception raise karo

class Age_error(Exception):
    pass

def check_age(age):
    if age < 18:
        raise Age_error("Underage user")
    return "Allowed"

print(check_age(27))
