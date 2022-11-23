'''
price = int(input("Enter the price of the bike"))
if price > 100000:
    print(f"You need to pay Rs {(15/100)*price}")
elif price > 50000 and price <= 100000:
    print(f"You need to pay Rs {(10/100) * price}")
else:
    print(f"You need to pay Rs {(5/100) * price}")
'''

'''
age1 = int(input("Enter age of person 1"))
age2 = int(input("Enter age of person 2"))
age3 = int(input("Enter age of person 3"))
age4 = int(input("Enter age of person 4"))
if age1<age2 and age1<age3 and age1<age4:
    print("person 1 is the youngest")
elif age2<age1 and age2<age3 and age2<age4:
    print("person 2 is the youngest")
elif age3<age1 and age3<age2 and age3<age4:
    print("person 3 is the youngest")
elif age4<age1 and age4<age2 and age4<age3:
    print("person 4 is the youngest")
'''

'''
age1 = int(input("Enter age of person 1"))
age2 = int(input("Enter age of person 2"))
age3 = int(input("Enter age of person 3"))
age4 = int(input("Enter age of person 4"))
if age1>age2 and age1>age3 and age1>age4:
    print("person 1 is the oldest")
elif age2>age1 and age2>age3 and age2>age4:
    print("person 2 is the oldest")
elif age3>age1 and age3>age2 and age3>age4:
    print("person 3 is the oldest")
elif age4>age1 and age4>age2 and age4>age3:
    print("person 4 is the oldest")
'''

'''
perc = int(input("Enter your percentage"))
if perc < 25:
    print("D")
elif perc >= 25 and perc <=45:
    print("C")
elif perc >= 45 and perc <=50:
    print("B")
elif perc >= 50 and perc <=60:
    print("B+")
elif perc >= 60 and perc <=80:
    print("A")
elif perc > 80:
    print("A+")
'''

'''
time = int(input("Enter time period of service"))
if time > 10:
    print("Your bonus is 10%")
elif time>=6 and time<=10:
    print("You bonus is 8%")
elif time < 6:
    print("Your bonus is 5%")
'''

'''
a = int(input("Enter a number"))
b = int(input("Enter a number"))
c = int(input("Enter a number"))
if (a > b and a < c) or (a < b and a > c):
    print(f"{a} is the second largest")
elif (b > a and b < c) or (b < a and b > c):
    print(f"{b} is the second largest")
elif (c > b and c < a) or (c < b and c > a):
    print(f"{c} is the second largest")
'''

'''
n=int(input("enter the num of days  "))
if n<=5:
    print ("the total charge is",n*2)
elif n>=6 and n<=10 :
    print ("the total charge is",n*3)
elif n>=11 and n<=15:
    print ("the total charge is",n*4)
else:
    print ("the total charge is",n*5)
'''

'''
time = int(input("Enter time of service in years"))
sal = int(input("Enter your salary"))
if time > 5:
    print(f"your salary after bonus is {sal + (sal*(5/100))}")
else:
    print("You do not deserve to get a bonus")
'''

'''
str1=input("Enter a string")
str2=input("Enter another string")
if (sorted(str1) == sorted(str2)):
    print("The strings are anagrams.")
else:
    print("The strings aren't anagrams.")
'''

'''
perc = int(input("Enter your percentage"))
if perc < 25:
    print("F")
elif perc >= 25 and perc <=45:
    print("E")
elif perc >= 45 and perc <=50:
    print("D")
elif perc >= 50 and perc <=60:
    print("C")
elif perc >= 60 and perc <=80:
    print("B")
elif perc > 80:
    print("A")
'''

