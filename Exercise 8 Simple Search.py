"""

Exercise 8: Simple Search

"""

# Declares Six Variables of Names From User Input
a = str(input("Enter Name One: ")).lower().strip()
b = str(input("Enter Name Two: ")).lower().strip()
c = str(input("Enter Name Three: ")).lower().strip()
d = str(input("Enter Name Four: ")).lower().strip()
e = str(input("Enter Name Five: ")).lower().strip()
f = str(input("Enter Name Six: ")).lower().strip()

# List of User Input Names
Names = [a, b, c, d, e, f]

# Prints Entered Names in Alphabetical and Numbered Order
Names.sort() 
print("\nEnterd Names List:")
for i in range(len(Names)):
    print(f"{i + 1}. {Names[i].title()}")
    
# Name Seaching User Input
Srch = str(input("\nWhich Name Do You Want To Search? ")).lower().strip()

print(f"Searching for -> {Srch.title()} <-")

# Checks if Searched Name is Valid or Not
if Srch in Names:
    print(f"-> {Srch.title()} <- is Available in List!")
else:
    print("Name is Invalid!")


