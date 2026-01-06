def count(n):
    if n == 0:        # base condition
        return
    print(n)
    count(n-1)        # recursive call

count(5)
