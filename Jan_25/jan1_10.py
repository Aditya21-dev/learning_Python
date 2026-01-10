# try:
#     a = 10
#     b = 0
#     print(a / b)
# except ZeroDivisionError:
#     print("Bhai zero se divide nahi hota ")


# try:
#     x = int(input("Number daalo: "))
#     y = int(input("Dusra number daalo: "))
#     print(x / y)

# except ValueError:
#     print("Sirf number daalo, alphabet nahi")

# except ZeroDivisionError:
#     print("Zero se divide karna mana hai")

# else:
#     print("Sab sahi chala")

# finally:
#     print("Program khatam, chai peelo")


# class UnderAgeError(Exception):
#     pass

# def check_age(age):
#     if age < 18:
#         raise UnderAgeError("Under 18 not allowed 🚫")
#     else:
#         print("Welcome sir 🎉")

# try:
#     check_age(15)
# except UnderAgeError as e:
#     print(e)


class na_balik(Exception):
    pass

def umar(n):
    if n < 18:
        raise na_balik('balik hoja h=fir aana bkl')
    else:
        print("wellcome.......!")

try:
    umar(7)
except na_balik as e:
    print(e)


print("hello")