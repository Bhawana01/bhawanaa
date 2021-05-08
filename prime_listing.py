def is_prime(n):
    i = 2
    while i*i <= n:
        if n%i == 0:
            return False
        i += 1
    return True

def print_prime(n):
    items = [2]
    i = 3
    while i <= n:  
        if is_prime(i):
            items.append(i)
        i += 1
    print(items)
    return items

def new_function2():
    a = [3,5,7,12,19,25,30,40,42]
    res1 = []
    # res2 = []
    res3 = []
    # b = [5,25,30,40]
    # div3= [3,12,30,42]
    for i in a:
        if i % 5 == 0:
            res1.append(i)
        else:
            res3.append(i)
        # if i % 3 == 0:
        #     res2.append(i)
    print(res1)
    print(res3)

def new_function():
    a = [3,5,7,12,19,25,30,40,42]
    result = []
    for i in a:
        if i % 5 == 0:
            result.append(i*i)
    print(result)


