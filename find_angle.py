def another_angle():
    print('\n\n************  Find another angle of Triangle **************')
    a = input('First angle')
    b = input('Second angle')
    a = int(a)
    b = int(b)
    c = 180 - (a + b)
    print('Third angle :', c)