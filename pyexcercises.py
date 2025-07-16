#Exercise 23: Create a simple countdown timer using a while loop.
"""
import time 
def countdown_timer(seconds):
    while seconds >0:
        print(f"time remaining :{seconds} seconds ")
        time.sleep(1) #pause for 1 second 
        seconds -=1
    print(" Time's up")
#get the coundown duration from the user
duration =5
countdown_timer(duration)


import time
def count_down(seconds):
  while seconds >0:
     print(f"time remaining :{ seconds} seconds")
     time.sleep(1)
     seconds-=1
  print("Time's Up!")
duration = 5
count_down(duration)

#Exercise 1: Create a function in Python
# demo is the function name 
def demo(name, age):
    print(name, age )
#call the function arguments
demo("joy", 20)

#Exercise 2: Create a function with variable length of arguments
#Write a program to create a function func1() that accepts a variable number of arguments and prints each of their values
def func1 (*args):
    for arg in args:
        print(arg)
# Call the function with variable number of arguments
func1(1,2,3,4)
func1(True, 3.21, 12, "ro")
func1(10,20,30)
func1()

#Exercise 3: Return multiple values from a function
def calculation(a,b):
   sum = a+b 
   mul = a*b
   sub = a-b
   return sum , mul, sub 
res= calculation(10,5)
print(res)
#Write a function calculation() that accepts two variables and calculates both their addition and subtraction.
#The function should then return both the sum and the difference in a single return statement

#Exercise 4: Create a function with a default argument
def show_employee(name,salary=9000):
    print(f"Name :{name} , salary:{salary}")
a=show_employee("Ben")
b=show_employee("Jovita")
#Exercise 5: Create an inner function

#Exercise 5: Create an inner function
#Create a program with nested functions to perform an addition calculation as follows:

#Define an outer function that accepts two parameters, a and b.
#Inside this outer function, define an inner function that calculates the sum of a and b.
#The outer function should then add 5 to this sum.
#Finally, the outer function should return the resulting value.

# outer function
def outer_fun(a, b):
    square = a ** 2

    # inner function
    def addition(a, b):
        return a + b

    # call inner function from outer function
    add = addition(a, b)
    # add 5 to the result
    return add + 5

result = outer_fun(5, 10)
print(result)

#Exercise 6: Create a recursive function

#Write a program to create a recursive function that calculates the sum of numbers from 0 to 10.
#A recursive function is a function that calls itself repeatedly.
def addition(num):
    if num:
        return num + addition(num -1)
    else:
        return 0
a= addition(10)
print(a)


#Exercise 7: Assign a different name to function and call it through the new name
def display_student(name,age):
    print(name,age)
#call using original name 
display_student("Minora", 19)
#assigns  a new name to the function
show_student= display_student
#call using the new name 
show_student("Minora", 19)

#Exercise 8: Generate a Python list of all the even numbers between 4 to 30
print(list(range(4,31,2)))

#Exercise 9: Find the largest item from list
a=[10,20,30,40,50,60,70,80,90]
print(max(a))

#Exercise 10: Call Function using both positional and keyword arguments
def describe_pet(animal_type, pet_name):
    print(f"animal {animal_type} : pet name {pet_name} ")
describe_pet("Hamester", "Harry") #calling the function using positionl arguments
describe_pet(animal_type=" cat", pet_name= " whiskers") #calling the function  using keyword argumnets

#Exercise 1: Print first 10 natural numbers using while loop
for i in range (1,11):
    print(i)
    
#Exercise 2: Print the following pattern
print(" Number Pattern")
# decide the number of rows 
rows= 5
#start = 1
#stop = row +1
#step =1
for i in range (1, rows+1, 1 ):
    for j in range ( 1, i+1):
        print(j, end=" ")
    print() # move to the next line after each row is printed 

#Exercise 3: Calculate sum of all numbers from 1 to a given number
s = 0 # stores the sum of all numbers
n = int(input(" enter a number :"))
for i in range ( 1, n+1, 1 ):
    s +=i  # add current variable to the sum 
print(" ")
print ( f" the sum is { s} ")

#Exercise 4: Print multiplication table of a given number
print(" Multiplication Table ")
num = int(input(" enter a number for multiplication table "))
for i in range (1, 11):
    print(f"{num } x {i} = {num*i}")

#Exercise 5: Display numbers from a list using a loop
num =[50, 75, 100, 105, 145, 160, 178, 190, 400, 505]
for item in num :
    if item > 500:
        break # the item is greater than 500 , exit the loop 
    elif item > 150:
        continue # the item is greater than 150, exit the current iteration 
    elif item % 5 == 0:
        print( item ) # display the item that is divisible by 5

#Exercise 6: Count the total number of digits in a number
number = int(input(" Enter the Number :"))
counter =0
while number !=0:
    number =number //10 # floor divsion # to reduce the last digit of the number 
    counter +=1 # increments the number by one 
print(" the total number of digits :", counter)

#Exercise 7: Print the following pattern
n= 5
k=6
for i in range ( 1 ,n+1):
    for j in range (k-i, 0, -1):
        print(j , end= " ")
    print() # move to the next line after each row is printed 

#Exercise 8: Print list in reverse order using a loop
l=[10, 20 ,30 ,40 ,50, 60, 70, 80, 90]
size =len(l)
for i in range(size-1, 0, -1):
    print(l[i], end =" ") # print the list in reverse order 


#Exercise 9: Display numbers from -10 to -1 using for loop
for i in range (-10, 0):
    print(i)

#Exercise 10: Display a message “Done” after the successful execution of the for loop
for i in range (5):
    print(i)
print("Done") # display the message after the loop is done executing

#Exercise 11: Print all prime numbers within a range
print(" the prime numbers are:")
start = 50
end = 100
for num in range (start, end +1): # check each number in range from start to end 
    if num>1: # checks if the number is greater thhan 1 
        for i in range (2, num): ## Try to divide by 2, 3, 4, ..., num-1
            if (num% i)==0:
                break # if the number is divisible by any number other than 1 and itself, it is not prime
        else:
             print(num)
       
#Exercise 12: Display Fibonacci series up to 10 terms
num1 , num2 =0, 1
print("fibonacci series :")
for i in range (10):
    print(num1, end =" ") #print next number of the series
    res =num1 +num2
    #update values
    num1 = num2
    num2  = res

#Exercise 13: Find the factorial of a given number
num = int(input("enter a given integer number :"))
factorial =1
if num < 0:
    print(" factorial for negative number does not exist ")
if num ==0:
        print(" the factorial is 1 ")
else:
    for i in range ( 1, num +1):
        factorial= factorial * i
    print(f" the factoriaal of {num } is {factorial}")
   
#Exercise 14: Reverse a integer number
num = int(input("enter a number to reverse :"))
reverse = 0 
while num!=0:
    digit = num%10
    reverse = reverse *10 + digit
    num = num//10
print(f" the reversed number is { reverse }") 
"""
#Exercise 15: Print elements from a given
#list present at odd index positions
my_list =[10,20,30,50,70 ,60]
for i in  my_list(1 : : 2):
    print(i , end ="")