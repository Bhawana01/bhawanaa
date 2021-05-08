def test():
# print("This is for practice!")
# print("This is an example of python!")
# print("We 're getting married very soon!")
# print(' We all \'re nepali!!')
# print(4 + 5)
# print(int('11') + 5)
# print(float('4.5') + 5)
# print(4**4)

# variables
# x, y = (4, 5)
# print(x)
# print(y)

#    while loop
#    condition = 1
#    while condition < 10:
#       print("While Loop :", condition)
#       condition += 1

# while True:
#    print("Doing stuff!")

# for loop
# exampleList  = {1,2,45,34,66, 23, 6, 99, 7}

# for eachNumber in exampleList:
#    print(eachNumber)
#    print("continue program")

# for x in range(1, 11):
   #    print(x)

# if-statement
#    x = 5
#    y = 8
#    z = 5
#    a = 3
#
#    if z < y > x > a:
#       print("y is greater than z and greater than x!")
#    if z <= x:
#       print('z is less than or equal to x!')
#    if z == x:
#       print("z is equal to x!")

# if-else
#    x = 5
#    y = 8
#    if x>y:
#       print("x is greater than y!")
#    if x < 55:
#       print("x is greater than 55!")
#    else:
#       print("x is not greater than y!")


# if-elif-else
#    x = 5
#    y = 10
#    z = 22
#
#    if x > y:
#       print("x is greater than y!")
#    elif x < z:
#       print("x is less than z!")
#    else:
#       print("if and elif(s) never ran!")

# functions
# test()

# function parameters
# def simple_addition(num1, num2):
#    answer = num1 + num2
#    print('num1 is ', num1)
#    print(answer)
#
# simple_addition(10.6,3)
#
# # function parameters defaults
# def sum(num1, num2):
#    pass
#
# sum(4,5)
#
# def simple(num1, num2=5):
#    print(num1, num2)
#
# simple(3)
#
# def basic_window(width,height,font='TNR',bgc='w',scrollbar=True):
#    print(width,height,font,bgc)
#
# basic_window(500, 300)


# global and local variables
#    x = 5
#    def example():
#       # print(x)
#       # print(x+5)
#       globx = x
#       print(globx)
#       globx += 5
#       print(globx)
#       return globx
#    x = example()
#    print(x)

# writing to file
#    text = "Sample Text to Save \nNew  Line!"
#    saveFile = open('exampleFile.txt', 'w')
#    saveFile.write(text)
#    saveFile.close()

# appending files
#    appendMe = "\n New bit of information"
#
#    appendFile = open('exampleFile.txt','a')
#    appendFile.write(appendMe)
#    appendFile.close()

   # read from a file
   # readMe = open("exampleFile.txt", 'r').read()
   # readMe = open("exampleFile.txt", 'r').readlines()
   # print(readMe)

   # classes
   class calcultor:
      def addition(x,y):
         add = x+y
         print(add)

      def subtraction(x,y):
         sub = x - y
         print(sub)

      def multiplication(x, y):
         mul = x * y
         print(mul)

      def division(x,y):
         div = x / y
         print(div)

   calcultor.multiplication(3,5)
   calcultor.addition(4,6)
   calcultor.subtraction(9,3)
   calcultor.division(55,11)

# getting from user
#    x = input("What is your name?")
#    print('Hello', x)

 # statistics(mean, median, Standard Deviation)
 #   import statistics
 #   example_list = [2,3,4,6,78,8,9,6,5,4]
 #   x = statistics.mean(example_list)
 #   print('Mean:',x)
 #   y = statistics.median(example_list)
 #   print('Median:',y)
 #   z = statistics.stdev(example_list)
 #   print('Standard Deviation:',z)
 #   a = statistics.variance(example_list)
 #   print('Variance:', a)

# module import syntax
#    import statistics as s
#    example_list = [2,22,34,34,434,55,55]
#    x = s.variance(example_list)
#    print('Varience:',x)
#
#    from statistics import variance
#    example_list = [2,22,34,34,434,55,55]
#    x = variance(example_list)
#    print(x)
#
#    from statistics import variance as v
#    example_list = [2,22,34,34,434,55,55]
#    x = v(example_list)
#    print(x)

# lists and tuples
#    x = [5,6,2,5,4,2,2,5,6,1]
#    y = [5,6,2,5,4,2,2,5,6,1]
#    # append = add
#    x.remove(x[2])
#    y.append(2)
#    print('X:',x)
#    print('y:', y)
#    print(x[0:3])
#    print(x[4:6])
#    print('Negative list:', x[-1], x[-2])
#    print('Index:', x.index(1))
#    print('Count:', x.count(6))
#    print(y[2],y[3],y[4])
# #    sorting
#    x.sort()
#    print('Sort:', x)

# multidimensional list
#    x = [2,3,4,5,6]
#    print(x)
#    x = [
#       [[2,3],[3,3]],
#       [[3,3],[3,4]],[[4,5],[5,7]],
#       [[5,6],[6,6]]
#       ]
#    print(x)
#    print(x[1][0][0])



# reading from a CSV spreadsheet
#    import csv
#
#    with open('example.csv') as csvfile:
#       readCSV = csv.reader(csvfile, delimiter=',')
#
#       dates = []
#       colors = []
#
#       for row in readCSV:
#          color = row[3]
#          date = row[0]
#
#          dates.append(date)
#          colors.append(color)
#
#       print(dates)
#       print(colors)
#
#       whatColor = input('What color do you wish to know the date of?')
#       coldex = colors.index(whatColor.lower())
#
#       theDate = dates[coldex]
#
#       print('The date of ', whatColor,'is the date')import csv
#
#    with open('example.csv') as csvfile:
#       readCSV = csv.reader(csvfile, delimiter=',')
#
#       dates = []
#       colors = []
#
#       for row in readCSV:
#          color = row[3]
#          date = row[0]
#
#          dates.append(date)
#          colors.append(color)
#
#       print(dates)
#       print(colors)
#
#       whatColor = input('What color do you wish to know the date of?')
#       coldex = colors.index(whatColor.lower())
#
#       theDate = dates[coldex]
#
#       print('The date of ', whatColor,'is:' theDate)

# multiline print
#    print('''
#    this is a multiline print!!
#    Hello!!
#    ================
#    |              |
#    |              |
#    |              |
#    |      Box     |
#    |              |
#    |              |
#    ===============
#
#    ''')
# Dictionaries
#    exDict = {'Bhawana':[24,'white'], 'Thakur':[33,'black'], 'Sadhana':[23,'Gahu Goro'], 'Bijay':[18,'Black Beauty']}
#
#    print(exDict)
#    exDict['Durga'] = 43
#    print(exDict)
#    exDict['Nama'] = [42,'  Beautiful']
#    print(exDict)
#    print(exDict['Bhawana'][1])

# built-in functions
#    exNum1 = -5
#    exNum2 = 5
#    print(abs(exNum1))
#
#    if abs(exNum1) == exNum2:
#       print('These are same!')
#
#    exNum3 = [5,2,3,7,8]
#    print(max(exNum3))
#    print(min(exNum3))
#    x = 2.54
#    print(round(x))
#    y = 5.222
#    print(round(y))
#    import  math
#    print(math.floor(x))
#    print(math.ceil(y))

# os module
#    import os
#    curDir = os.getcwd()
#    print(curDir)
#    # make new folder/create new folder
#    os.mkdir('newDir')
#    import  time
#    time.sleep(10)
#    os.rename('newDir','newDir2')
#    time.sleep(10)
#    # remove
#    os.rmdir('newDir2')


# sys-module
   import sys
   sys.stderr.write('This is stderr text \n')
   sys.stderr.flush()
   sys.stdout.write('This is stdout text \n')
   # print(sys)
   print(sys.argv)

# urllib module
   import urllib.request
   import urllib.parse

   # x = urllib.request.urlopen('https://www.google.com/')
   # view source code of this above url
   # print(x.read())


   # url = "https://pythonprogramming.net/basic"
   # values = {'s':'basic',
   #           'submit':'search' }
   # data = urllib.parse.urlencode(values)
   # data = data.encode('utf-8')
   # req = urllib.request.Request(url,data)
   # resp = urllib.request.urlopen(req)
   # respData = resp.read()
   #
   # print(respData)

   try:
      x = urllib.request.urlopen('https://www.google.com/search?q=test')
      print(x.read())

   except Exception as e:
      print(str(e))

   # try:
   #    url = 'https://www.google.com/search?q=test'
   #    headers = {}
   #    headers['User-Agent']

#    regular expression / regex with re
   import re
   exampleString = '''
   Thakur is 33 years old, and his wife is 24 years old.
   And his father is 59 years old, and his mother  is 55 years old. 
   '''
   ages = re.findall(r'\d{1,3}', exampleString)
   names = re.findall(r'[A-Z][a-z]*', exampleString)

   print(ages)
   print(names)

   ageDict = {}
   x = 0
   for eachName in names:
      ageDict[eachName] = ages[x]
      x +=1
   print(ageDict)

# parsing websites with re and urllib
   import urllib.request
   import urllib.parse
   import re

   url = "https://pythonprogramming.net/"
   values = {'s':'basic',
             'submit':'search'}
   data = urllib.parse.urlencode(values)
   data = data.encode('utf-8')
   req = urllib.request.Request(url, data)
   resp = urllib.request.urlopen(req)
   respData = resp.read()

   # print(respData)

   paragraphs  = re.findall(r'<p>(.*?)</p>', str(respData))
   for eachP in paragraphs:
      print(eachP)