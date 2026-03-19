#Import
import random

x=random.randint(1,100) #random integer selected from 1-100

print("welcome to the number guessing game!")
print("i have selected a number between 1 and 100. can you guess it?")
while True:
    guess=int(input("Enter a number ")) #converts user's input to integer
    if guess==x: #if guess is number
        print("CONGRATULATIONS YOU GUESSED IT CORRECTLY")
        break #program ends
    elif guess>x: #if guess is higher than number
        print("too high")
        continue #program still runs
    elif guess<x: #if guess is neither
        print("too low")
        continue #program still runs
