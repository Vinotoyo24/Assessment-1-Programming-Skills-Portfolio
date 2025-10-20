"""

Exercise 5: Days of the Month

"""
# Month Dictionary
Month = {1 : "January", 
         2 : "February", 
         3 : "March", 
         4 : "April", 
         5 : "May", 
         6 : "June", 
         7 : "July", 
         8 : "August", 
         9 : "September", 
         10 : "October", 
         11 : "November", 
         12 : "December"}

# Days Dictionary of Corresponding Month
Days = {1 : 31,
        2 : 28,
        3 : 31,
        4 : 30,
        5 : 31,
        6 : 30,
        7 : 31,
        8 : 31,
        9 : 30,
        10 : 31,
        11 : 30,
        12 : 31}

# Input
A = int(input("Which Month Number You Want twin: "))

# Declares a Variable of Valid Month
B = A in Month

# Checks if Month is Valid or not
if B == True: # Prints the Number of Days to the Corresponding Month
    print("Your Month is Valid ")
    print("Month:", Month[A], "\nDays:", Days[A])
else: # Month is not Valid
    print("Your Month is not Valid!")
    




