#Project: String Manipulation Tool
#Create a Python script that takes a string as input and performs various string manipulation operations based on user choice.

print("WELCOME TO STRING MANIPULATION TOOL")
user_string = input("Enter string to manipulate:")

print("Your entered string is:" + user_string)
print("Please select string manipulation option:")
print("""Option 1: Convert the string to uppercase
Option 2: Convert the string to lowercase
Option 3: Slice the string from a start index to an end index
Option 4: Calculate the length of the string
Option 5: Loop through each character in the string and display it on a new line""")

option_input = int(input("Enter any option (1-5): ")) 

if(option_input == 1):
   print(user_string.upper())
elif(option_input == 2):
    print(user_string.lower())
elif(option_input == 3):
    start = int(input("Enter start index: "))
    end = int(input("Enter end index: "))
    print(user_string[start:end])
elif(option_input == 4):
    print(len(user_string))
elif(option_input == 5):
    for x in user_string:
        print(x)
else:
    print("You have selected invalid option! please select again")



