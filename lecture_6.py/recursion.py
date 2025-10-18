def show(n):
    a = 123
    if(n == 0):
        return
    print(n)
    show(n-1)
show(5)