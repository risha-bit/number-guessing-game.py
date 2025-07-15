
# Number guessing game 
# This is a simple number guessing game where the user has to guess a number between a given range.
# The user has 6 chances to guess the number correctly.
import random
print("Welcome to Guessing Game !!, You have 6 chances to guess it . Let's Start !!!")
low = int(input("enter the number where it should start from :"))
high= int(input("enter the number where it should end at :"))
print(f"you are supposed to guess a number between {low} to {high}")
num = random.randint(low,high)

gc = 0 #guess counter
ch= 7 #total allowed chances
while gc< ch :
    gc+=1
    guess = int(input("enter the guess number :"))
    if guess <low or guess>high :
       print(f" invalid input ! enter a valid number ")
       gc =-1
       continue

    if guess == num :
      print(f"the guessed number is {guess} , you have to guess it in {gc} attempts ")
      break
    elif abs(guess- num )==1:
       print(f"So close ! you're just 1 away!!") 
    elif abs(guess- num)<= 3:
       if guess< num:
          print(" very close ! try guessing higher number ")
       else:
          print(" very close ! try guessing a lower number") 
       
    elif guess!=num and gc>= ch:
       print(f" sorry !You have lost all chances to guess the number!! better luck next time ")
    elif guess< num:
      print(" The guessed  number is too low!! Try guessing higher number ")
    elif guess >num:
       print(f" The guessed number is too high!! Try guess a lower number ")
       
