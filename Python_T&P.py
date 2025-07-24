#Q1. Write a program to check if a given number is Positive, Negative or Zero.
import math

number = int(input("Enter the numer"))
if(number>0):
    print(number + "is Positive")
elif(number<0):
    print(number + "is negative")
else:
    print("is Zero")


#Q2. Write a program to check if a given number is odd or even.
number = int(input("Enter the numer"))
if(number // 2 == 0):
    print("number is Even" )
elif(number // 2 != 0):
    print("Number is Odd")
else:
    print("Invalid number")


#Q3. # Given two non-negative values, print true if they have the same last digit, such as with 27 and 57

number = int(input("Enter Desired Number"))
if(number//10 == 70):
    print(True)
else:False

#Q4. Write a program to print numbers from 1 to 10 in a single row with one tab space.
n = 10
for i in range(0, n):
    print(i)
    i+=1


#Q5. Write a program to print even numbers between 23 and 57. Each number should be printed in a seperate row.

for i in range(23, 57, 2):
    print(i)



#Q6. Write a program to check if a given number is prime or not.
N= int(input("Enter a number"))
count = 0
for i in range(1, N):
    if(N%i == 0):
        count += 1
    if(count == 2):
        print("YES")
    else:
        print("Not a prime number")


#ANOTHER OPTIMAL APPROACH

N = int(input("Enter the number"))
M = math.sqrt(N)
for i in range(0, M):
    if(M % i == 0):
        count += 1
        if(M/ i != i):
            count += 1
if(count == 2):
    print("Pirme")
else: print("Not Prime")


# print prime numbers between 10 to 99
num = 10
while num <= 99:
    is_prime = True
    if num < 2:
        is_prime = False
    else:
        i = 2
        while i * i <= num:
            if num % i == 0:
                is_prime = False
                break
            i += 1
    if is_prime:
        print(num, end=' ')
    num += 1



#WAP to print sum of all Digits of a given number.
num = int(input("Enter the number"))
sum_digits = 0

while num > 0:
    digit = num % 10
    sum_digits += digit
    num = num // 10

print("Sum of digits:", sum_digits)




#WAP to reverse a given number and print
num = int(input("Enter the number"))
reverse = 0
while num>0:
    digit = num%10
    reverse = reverse*10 + digit
    num = num//10

print(reverse)











#1.	create a python program that asks the user how far they want to travel.
# if they want to travel less than three miles tell them to ride Bicycle.
# if they want to travel more than three miles, but less than three hundred miles, tell them to ride Motor-cycle.
# if they want to travel three hundred miles or more tell them to driver Super-Car.

asking_user = int(input("How far would you like pt travel in mies?"))
if(asking_user<=3):
    print("I suggest you to walk")

elif(300<asking_user>3):
    print("i sugget you to ride motor cycle")

else:
    print("I suggest super-car to your destination")







#2.	Let's assume you are planning to use your python skills to build an App for Mobile.
#You decide to host your application on servers running in the cloud. you pick a hosting provider that charges $0.51 per hour. you will launch your services using one server and want to know how much it will cost to operate per day, per week, per month.
#Write a python program that displays the answers to the following questions:
#How much does it cost to operate one server per day?
#How much does it cost to operate one server per week?
#How much does it cost to operate one server per month?
#How much days can I operate one server with $918?

hourly_rate = 0.51

cost_per_day = hourly_rate * 24
cost_per_week = cost_per_day * 7
cost_per_month = cost_per_day * 30

budget = 918
days_with_budget = budget / cost_per_day
print(f"Cost to operate one server per day: ${cost_per_day:.2f}")
print(f"Cost to operate one server per week: ${cost_per_week:.2f}")
print(f"Cost to operate one server per month (30 days): ${cost_per_month:.2f}")
print(f"With ${budget}, you can operate one server for approximately {days_with_budget:.2f} days.")
