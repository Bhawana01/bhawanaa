# n! = n* (n-1)* (n-2)* ....*1
# 4! = 4*3*2*1
def factorial(n):
    ans = None
# single line to  find factorial
# return 1 if(n == 1 orr n == 0) else  n * factorial(n-1);

    if n < 0:
        ans = 0
    elif n == 0 or n == 1:
        ans = 1
    else:
        fact = 1
        while(n > 1):
            fact *= n
            # print() n = n-1
            n -= 1
        ans =  fact
    return ans
# driven code
# num = 5
# print("Factorial of", num, "is", factorial(num))
