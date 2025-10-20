"""
Exercise 4: Primitive Quiz 

"""

# Asks and Declares a Variable for the user input for the Capital for France
Capital = str(input("What is the Capital of France? "))

#Checks if Capital condition is "Paris" or "paris"
if Capital == "Paris" or Capital == "paris":
    print("The capital of France is: ", Capital, ", Correct")
else: #if the answer is neither the two...
    print("The capital of France is: ", Capital, ", Incorrect")
