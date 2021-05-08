def find_max():
    lst = [3, 2, 5, 8, 9, 6]
    mx_num = None
    for item in lst:
        if mx_num is None:
            mx_num = item
        else:
            if item > mx_num:
                mx_num = item
    print(mx_num)


def find_min():
    lst = [3, 5, 22, 43, 56, 1, 6, 10]
    mn_num = None
    for item in lst:
        if mn_num is None:
            mn_num = item
        else:
            if item < mn_num:
                mn_num = item
    print(mn_num)


def count_numbers():
    lst = [3, 5, 8, 12, 14, 29, 40, 15, 18, 2, 20]
    count = 0
    for item in lst:
        count += 1
    print(count)

def check_numbers():
    x = input('First Number : ')
    y = input('Second Number :')
    if x == y:
        print('Two numbers are equal.')
    else:
        print('Two numbers are not equal.')


def even_odd():
    num = int(input('Enter Number :'))
    if num % 2 == 0:
        print('{} is Even' .format(num))
    else:
        print('{} is Odd' .format(num))


def check_triangle(a, b, c):
    if a == b and b == c and c == a:
        print('This is an equilateral triangle.')
    elif a == b or b == c:
        print('This is an isosceles triangle.')
    else:
        print('This is scalene triangle.')


def check_vowel():
    ch = input('Enter character :')
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
        print(f'The given character  {ch} is a vowel.')
    else:
        print(f'The given character {ch} is a consonant.')


def count_vowel():
    wrd = input('Enter word :')
    count = 0
    for i in wrd:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
            count += 1
    print(f'Vowels : {count} ')


def square_number_sum():
    n = 5
    sm = 0
    for item in range(1, n+1):
        sqr = item ** 2
        sm += sqr
    print(f'{n} terms of square natural number : {sqr}')
    print(f'And their sum is {sm}')


def month_no_name():
    mth = int(input('Enter month number :'))
    if mth == 1:
        print('January')
    elif mth == 2:
        print('February')
    elif mth == 3:
        print('March')
    elif mth == 4:
        print('April')
    elif mth == 5:
        print('May')
    elif mth == 6:
        print('June')
    elif mth == 7:
        print('July')
    elif mth == 8:
        print('August')
    elif mth == 9:
        print('September')
    elif mth == 10:
        print('October')
    elif mth == 11:
        print('November')
    else:
        print('December')


def area_rectangle():
    l = int(input('Enter length :'))
    b = int(input('Enter breadth:'))
    area = l * b
    print(f'Area of rectangle is {area}')


def perimeter_rectangle():
    l = int(input('Enter length :'))
    b = int(input('Enter breadth :'))
    perimeter = 2 * (l + b)
    print(f'Perimeter of rectangle is {perimeter}')



