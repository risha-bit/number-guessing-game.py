import random
name = input("Enter your name ?:")
print("Good luck !! Next Time ")
words= ["earbuds", "Phone", "laptop", "pen", "window", "charger", "table",
        "air"]
print(words)
word =random.choice(words) #randomly select a word from the list
print("guesss the character in the word")
guesses =' '#empty string to tore the guessed characters 
turns =12 #the number of chances the user has to guess the word
while turns > 0:
    failed = 0 # count the number of failed attempts
    for char in word :
        if char in guesses:
            print(char , end =" ")
        else:
            print("__", end =" ")
            failed +=1
    print() # for better formatting
    if  failed == 0: # if failed is 0 , it means the user has guessed the word
       print("You Win")
       print(" the word is :", word)
       break
    guess = input(" guess the character:")
    guesses += guess #adds the new guesses to the previous guesses
    if guess not in word :
       turns -= 1
       print("Wrong ")
       print(" you have ", turns , "turns left")
    if turns ==0:
        print(" you lose ")
        print(" the word was :", word)

