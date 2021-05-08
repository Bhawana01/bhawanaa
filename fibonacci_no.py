def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect Input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        # return fibonacci(n-1)+fibonacci(n-2)
        for i in range(2, n):
            c = a+b
            print("value of c:", c)
            a = b
            # print("a:",a)
            b = c
            # print("b:",b)
        return b