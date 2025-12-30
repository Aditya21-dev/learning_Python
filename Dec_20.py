from functools import reduce

# Tumhare paas students ke marks hain.
#     Sirf pass students (>=40) lo
#     Grace rule: agar marks 35–39 ke beech ho → +5 add karo
#     Final list return karo

marks = [78, 35, 39, 12, 90, 41, 33]

result = list(
    map(lambda x:x+5 if x>=35 and x<=39 else x ,
        filter(lambda x: x>=35,marks))
)

print(result)



# E-commerce site ka total bill nikalo
#     Prices list hai
#     10% discount agar total > 5000

prices = [1200, 800, 1500, 2000]
total = reduce(lambda x,y:x+y,prices)
final = total=total/100*10 if total>5000 else total
print(final)



# Ek generator banao jo even invoice numbers generate kare upto n

def even_genrator(n):
    for i in range(2,n+1,2):
        yield i

for inv in even_genrator(10):
    print(inv)