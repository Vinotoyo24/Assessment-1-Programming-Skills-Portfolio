"""

Exercise 6: Brute Force Attack

"""

# Declares Correct Password Variabke
password = "12345"

# Declares User Input Variable
setpassIN = ""

# Declares Max Tries of Password
# Prints Available Tries
count = 5
print(f"You have: {count} tries")

# Checks if Tries is Valid 
while count > 0:
    setpassIN = input("\nEnter Password: ")
    if setpassIN == password: # Checks if Password is correct and breaks loop
        print("Correct Password!")
        break
    else: # Checks if Password is Incorrect and Uses Tries each Iterations
        count -= 1
        print(f"Incorrect Password \nYou have: {-count} Tries Left")
        if count > 0 : # Try Again Message
            print("Please Try Again!")
        if count == 0: # Checks if Tries Have Ran Out
            print("You have Ran Out of Tries")
            print("Locking...")
        

        