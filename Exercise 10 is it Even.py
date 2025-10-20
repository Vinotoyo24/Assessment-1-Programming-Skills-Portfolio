"""

Exercise 10: Is it Even?

"""

#Function For Determining Even or Odd
def Even_or_Odd(a):
    print(a)
    if a % 2 == 0: #if input number returns a Remainder of 0 
        return print("Number is Even") #Returns as Even
    else:
        return print("Number is Odd") #Returns as Odd

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Main Function
while True:
    i = float(input("Input a Number: ")) #User Input
    Even_or_Odd(i) #Declares User Input Into the Arguement of Even_or_Odd() Function
