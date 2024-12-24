#this is global variable
x = "awesome"

#This is simple function which display some text
def display():
    #here global variable is being used to display message
    print("python is "+ x)
display()
#This is another simple function but this time with the use of local variable
def display1():
    #this is local variable
    x = "fantastic"
    #this time it will use local x instead of global x.
    print("python is "+ x)

display1()

