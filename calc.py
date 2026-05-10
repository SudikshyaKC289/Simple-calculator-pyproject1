num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
55#step 1: fuctions for operator
#function to add two numbers 
def add (num1, num2):
    return num1+num2
#function to subtract two numbers
def subtract(num1, num2):
    return num1-num2
#function to multiply two numbers
def multiply (num1, num2):
    return num1*num2
#function to divide two numbers
def divide (num1, num2):
    return num1/num2
#function to subtract two numbers
def average (num1, num2):
    return (num1+num2)/2

#step 2: user input
print ("Select the operator for any two numbers:\n" "1.Addition\n" "2.Subtraction\n""3.Multipication\n""4.Division\n""5.Average\n")
select=int(input("select any  operator from 1 to 5: "))


#step 3 : Printing the result
if select == 1:
    print("Addition of two numbers is:",add(num1,num2))

elif select == 2:
    print("Subtraction of two numbers is:",subtract(num1,num2))

elif select == 3:
    print("Multiplication of two numbers is:",multiply(num1,num2))

elif select == 4:
    print("Division of two numbers is:",divide(num1,num2))

elif select == 5:
    print("Average of two numbers is:",average(num1,num2))

else:
    print ("INVALID OPERATION FAHHH !!!! \n Please select between 1 ,2 ,3 ,4 ,and 5")

