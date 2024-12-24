#Project: Random Number Generator
#Create a program that generates a random number between 1 and 100, then prints out the number along with its data type.

import random

random_number = random.randrange(1,100)

print("Random Number is: ", random_number);
print("The number type is: ", type(random_number))