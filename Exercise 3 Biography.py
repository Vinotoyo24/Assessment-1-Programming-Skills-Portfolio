"""

Exercise 3: Biography

"""

#Declares User Input Variables for Name, Home, And Age
Name = str(input("Enter Name: "))
Home = str(input("Enter HomeTown: "))
Age = (input("Enter Age: "))

#Prevents User From Entering String Value
while Age.isdigit() == False:
    print("\nEnter A Valid Age")
    Age = (input("Enter Age: "))

# Biography Dictionary
Biography = {'name' : Name,
             "Hometown" : Home,
             "Age" : Age}

# Prints The Output for Entered Biography
print("\n-> Biography: <-")
user = Name.split() #Splits Lines of Enter User Name

# Handles Multiple Lines of Name
if len(user) > 1:
    #Prints Biography With First and last name, Hometown, and Age.
    print(f"First Name: {user[0]} \nLast Name: {user[-1]} \nHomeTown: {Home} \nAge: {Age}")
else:
    #Prints Biography Name, Hometown, and Age.
    print(f"Name: {user[0]} \nHomeTown: {Home} \nAge: {Age}")