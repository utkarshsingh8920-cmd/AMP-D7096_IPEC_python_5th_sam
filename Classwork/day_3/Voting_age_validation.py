"""----------------Voting Age Validation Program----------------------
 Write a program for check the person is eligibal for voting or not
  if age is less then 18 you are elibible to vote """
#------------------Coding----------------------------
age = int(input("Enter your age: "))
if age<0:
    exit("age can not negative")
#-------------Check validation-----------------------    
if age >= 18:
    print("-----------------------------------------")
    print("You are eligible to vote.")
    print("-----------------------------------------")
else:
    print("-----------------------------------------")
    print("You are not eligible to vote.")
    print("-----------------------------------------")
"""Output : 
Enter your age: 34
-----------------------------------------
You are eligible to vote.
----------------------------------------
"""