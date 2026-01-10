# f=open('00.html','x')
# print(f.name)
# print(f.mode)
# print(f.writable())
# print(f.readable())
# print(f.closed)
# print(f.encoding)


# with open("t2.txt",'x') as f:
#     pass
# print(f.name)
# print(f.closed)
# print(f.writable())
# print(f.readable())
# print(f.encoding)

f = open("t1.txt",'a')
print(f.name)
print(f.closed)
print(f.writable())
print(f.readable())
print(f.encoding)


with open("t1.txt",'w+') as f:
    f.write("hello chandu ...........! heee heee")
    f.seek(0) 
    print(f.read())
    print(f.tell())



