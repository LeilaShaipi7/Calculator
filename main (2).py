#Define four subroutines - add, subtract, multiply, divide that add multiply etc two numbers and return the result. Each should have two integer number arguments.
#The user is asked to input two numbers.  These numbers will be passed as arguments into one of the subroutines.
#The user is asked to input 1 to add, 2 to subtract etc.
#If they input 1, call the ‘add’ subroutine, input 2 calls the ‘subtract’ subroutine etc
#Output the returned result as part of a sentence.


def add_num(num1, num2):
  return num1 + num2

def sub_num(num1, num2):
  return num1 - num2

def mul_num(num1, num2):
  return num1 * num2

def div_num(num1, num2):
  if num2 == 0:
    return "cannot be divided by zero"
  return num1 / num2

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

userInput = input("Enter 1 to add, 2 to subtract, 3 to multiply, or 4 to divide: ")

if userInput == "1":
  print("The answer is: " + str(add_num(num1, num2)))

elif userInput == "2":
  print("The answer is: " + str(sub_num(num1, num2)))

elif userInput == "3":
  print("The answer is: " + str(mul_num(num1, num2)))

elif userInput == "4":
  print("The answer is: " + str(div_num(num1, num2)))

else:
  print("Invalid choice")

