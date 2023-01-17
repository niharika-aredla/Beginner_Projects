import random
import math

#ask user for a range
lower = int(input('Select your lower bound : '))
upper = int(input('Select your upper bound : '))

#computer generated random number
#tracking guess count
num = random.randint(lower,upper)
range = upper-lower
count = 0

#calculating number of guess based on user input range
#takes log of the range+1 and base 2
print('You have '+ str(round(math.log(range + 1, 2))) + ' guesses.')

#while there are guesses remaining
#keep asking for user input
while count < math.log(range+1,2):
    count += 1

    guess = int(input("Guess a number in your selected range : "))

#answered under guess limit, break out of while loop
    if num == guess:
        print('Congratulations!! You guessed in ' + str(count) + ' tries.')
        break

#testing for incorrect answers while under guess limit
    elif num < guess:
        print("You guessed too high!")
    elif num > guess:
        print("You guessed too low!")

#out of guess limit
if count >= math.log(range+1,2):
    print("You ran out of your turns!!\nThe number is " + str(num))
